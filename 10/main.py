with open('10/input.txt') as f:
    lines = f.read().splitlines()

def solve_part_1():
    total_presses = 0
    for line in lines:
        if not line.strip(): continue

        # Parse Lights
        l_start, l_end = line.find('[') + 1, line.find(']')
        lights = line[l_start:l_end]
        target_mask = sum(1 << i for i, c in enumerate(lights) if c == '#')

        # Parse Buttons
        # Extract string between ] and {
        t_start = line.find('{')
        mid = line[l_end+1:t_start]
        buttons = []
        
        for chunk in mid.split('('):
            if ')' not in chunk: continue
            nums = [int(x) for x in chunk.split(')')[0].split(',')]
            mask = 0
            for n in nums: mask |= (1 << n)
            buttons.append(mask)

        # BFS
        queue = [(0, 0)] # state, presses
        visited = {0}
        if target_mask != 0:
            while queue:
                state, presses = queue.pop(0)
                if state == target_mask:
                    total_presses += presses
                    break
                
                for btn in buttons:
                    nxt = state ^ btn
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, presses + 1))
    return total_presses

def solve_part_2():
    total_presses = 0
    for line in lines:
        if not line.strip(): continue

        # Parse Targets
        t_start, t_end = line.find('{') + 1, line.find('}')
        targets = [int(x) for x in line[t_start:t_end].split(',')]
        num_eq = len(targets)

        # Parse Buttons
        l_end = line.find(']')
        mid = line[l_end+1:t_start]
        buttons = []
        
        for chunk in mid.split('('):
            if ')' not in chunk: continue
            nums = [int(x) for x in chunk.split(')')[0].split(',')]
            col = [0] * num_eq
            for n in nums:
                if n < num_eq: col[n] = 1
            buttons.append(col)

        # Gaussian Elimination (Float)
        num_vars = len(buttons)
        matrix = []
        for r in range(num_eq):
            row = [float(buttons[c][r]) for c in range(num_vars)] + [float(targets[r])]
            matrix.append(row)

        pivot_cols = []
        free_cols = []
        curr_row = 0

        for col in range(num_vars):
            if curr_row >= num_eq:
                free_cols.append(col)
                continue
            
            pivot_row = -1
            for r in range(curr_row, num_eq):
                if abs(matrix[r][col]) > 1e-9:
                    pivot_row = r
                    break
            
            if pivot_row == -1:
                free_cols.append(col)
                continue
            
            matrix[curr_row], matrix[pivot_row] = matrix[pivot_row], matrix[curr_row]
            pivot_val = matrix[curr_row][col]
            for c in range(col, len(matrix[0])):
                matrix[curr_row][c] /= pivot_val
            
            for r in range(num_eq):
                if r != curr_row and abs(matrix[r][col]) > 1e-9:
                    factor = matrix[r][col]
                    for c in range(col, len(matrix[0])):
                        matrix[r][c] -= factor * matrix[curr_row][c]
            
            pivot_cols.append(col)
            curr_row += 1

        consistent = True
        for r in range(curr_row, num_eq):
            if abs(matrix[r][-1]) > 1e-9:
                consistent = False
                break
        if not consistent: continue

        pivots = []
        for i in range(len(pivot_cols)):
            const = matrix[i][-1]
            coeffs = []
            for fc in free_cols:
                if abs(matrix[i][fc]) > 1e-9:
                    coeffs.append((matrix[i][fc], fc))
            pivots.append((const, coeffs))

        min_local = float('inf')
        
        def search(idx, current_free):
            nonlocal min_local
            current_sum = sum(current_free.values())
            if current_sum >= min_local: return

            if idx == len(free_cols):
                valid = True
                total = current_sum
                for const, coeffs in pivots:
                    val = const
                    for c, fc in coeffs:
                        val -= c * current_free[fc]
                    
                    if val < -1e-9:
                        valid = False; break
                    nearest = round(val)
                    if abs(val - nearest) > 1e-9:
                        valid = False; break
                    total += int(nearest)
                
                if valid:
                    min_local = min(min_local, total)
                return

            fc = free_cols[idx]
            # Heuristic bounds
            low, high = 0, 300
            
            for val in range(low, high + 1):
                current_free[fc] = val
                search(idx + 1, current_free)
                del current_free[fc]

        search(0, {})
        if min_local != float('inf'):
            total_presses += min_local

    return total_presses

if __name__ == '__main__':
    print(f"Part 1: {solve_part_1()}")
    print(f"Part 2: {solve_part_2()}")
