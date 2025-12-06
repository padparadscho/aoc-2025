with open('06/input.txt', 'r') as f:
    content = f.read()
lines = content.splitlines()


def solve_part_1(lines):
    # Parse the input into a grid of tokens
    grid = []
    for line in lines:
        tokens = [t for t in line.split() if t]
        grid.append(tokens)

    num_cols = max(len(row) for row in grid)

    total = 0
    for col in range(num_cols):
        numbers = []
        # Extract numbers from the rows above the operator
        for row in range(len(grid) - 1):
            if col < len(grid[row]) and grid[row][col] != '':
                numbers.append(int(grid[row][col]))
        
        # The last row contains the operator
        op = grid[-1][col]
        
        if op == '*':
            result = 1
            for num in numbers:
                result *= num
        elif op == '+':
            result = 0
            for num in numbers:
                result += num
                
        total += result

    print(f"Part 1 Solution: {total}")


def solve_part_2(lines):
    # Pad lines to max length to form a proper grid
    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len) for line in lines]
    
    num_rows = len(grid)
    num_cols = max_len
    
    # Identify separator columns (all spaces)
    problem_blocks = []
    current_block = []
    
    for col in range(num_cols):
        is_separator = True
        for row in range(num_rows):
            if grid[row][col] != ' ':
                is_separator = False
                break
        
        if is_separator:
            if current_block:
                problem_blocks.append(current_block)
                current_block = []
        else:
            current_block.append(col)
            
    if current_block:
        problem_blocks.append(current_block)
        
    total_sum = 0
    
    for block in problem_blocks:
        operator = None
        numbers = []
        
        # Find operator in the last row
        for col in block:
            char = grid[num_rows-1][col]
            if char in ('+', '*'):
                operator = char
        
        if operator is None:
            continue
            
        # Extract numbers vertically
        for col in block:
            digit_str = ""
            for row in range(num_rows - 1):
                char = grid[row][col]
                if char.isdigit():
                    digit_str += char
            
            if digit_str:
                numbers.append(int(digit_str))
                
        if operator == '+':
            res = sum(numbers)
        elif operator == '*':
            res = 1
            for n in numbers:
                res *= n
        else:
            res = 0
            
        total_sum += res
        
    print(f"Part 2 Solution: {total_sum}")


if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)