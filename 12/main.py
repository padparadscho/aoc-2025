def solve():
    with open('12/input.txt') as f:
        lines = f.read().splitlines()

    # Parse shapes
    shapes = []
    current_shape = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        
        if ':' in line and not 'x' in line: # Shape header "0:"
            if current_shape:
                shapes.append(current_shape)
                current_shape = []
            i += 1
            while i < len(lines) and lines[i].strip() and ':' not in lines[i] and 'x' not in lines[i]:
                current_shape.append(lines[i])
                i += 1
            continue
        
        if 'x' in line: # Region line "36x44: ..."
            if current_shape:
                shapes.append(current_shape)
                current_shape = []
            break
        i += 1
        
    # Process shapes into coordinate sets
    shape_variants = []
    for s_idx, shape_grid in enumerate(shapes):
        base_coords = set()
        for r, row in enumerate(shape_grid):
            for c, char in enumerate(row):
                if char == '#':
                    base_coords.add((r, c))
        
        variants = []
        # Rotate
        curr = base_coords
        for _ in range(4):
            # Normalize
            min_r = min(r for r, c in curr)
            min_c = min(c for r, c in curr)
            norm = frozenset((r - min_r, c - min_c) for r, c in curr)
            variants.append(norm)
            
            # Rotate 90 deg clockwise: (r, c) -> (c, -r)
            curr = set((c, -r) for r, c in curr)
            
        # Flip
        curr = set((r, -c) for r, c in base_coords)
        for _ in range(4):
            min_r = min(r for r, c in curr)
            min_c = min(c for r, c in curr)
            norm = frozenset((r - min_r, c - min_c) for r, c in curr)
            variants.append(norm)
            
            curr = set((c, -r) for r, c in curr)
            
        unique_variants = sorted(list(set(variants)), key=lambda x: (len(x), list(x)))
        # Precompute dimensions for each variant
        final_variants = []
        for v in unique_variants:
            h = max(r for r, c in v) + 1
            w = max(c for r, c in v) + 1
            final_variants.append({'coords': v, 'h': h, 'w': w})
        shape_variants.append(final_variants)

    # Parse regions and solve
    solved_count = 0
    
    # Pre-calculate shape areas
    shape_areas = []
    for s in shapes:
        area = sum(row.count('#') for row in s)
        shape_areas.append(area)

    start_regions_idx = i
    for line_idx in range(start_regions_idx, len(lines)):
        line = lines[line_idx]
        if not line.strip(): continue
        
        parts = line.split(': ')
        dims = parts[0].split('x')
        W, H = int(dims[0]), int(dims[1])
        counts = [int(x) for x in parts[1].split(' ')]
        
        # Check total area first
        total_present_area = sum(counts[i] * shape_areas[i] for i in range(len(counts)))
        if total_present_area > W * H:
            continue # Impossible
            
        # Prepare list of presents to place
        presents = []
        for s_idx, count in enumerate(counts):
            for _ in range(count):
                presents.append((s_idx, shape_variants[s_idx]))
        
        # Sort presents by area descending
        presents.sort(key=lambda x: shape_areas[x[0]], reverse=True)
        
        # Backtracking solver
        grid = [[False for _ in range(W)] for _ in range(H)]
        
        def can_place(r, c, variant):
            if r + variant['h'] > H or c + variant['w'] > W:
                return False
            for pr, pc in variant['coords']:
                if grid[r + pr][c + pc]:
                    return False
            return True
            
        def place(r, c, variant, val):
            for pr, pc in variant['coords']:
                grid[r + pr][c + pc] = val

        def solve_recursive(p_idx):
            if p_idx == len(presents):
                return True
            
            s_idx, variants = presents[p_idx]
            
            # Try to place the present in every possible valid position
            for r in range(H):
                for c in range(W):
                    for v in variants:
                        if can_place(r, c, v):
                            place(r, c, v, True)
                            if solve_recursive(p_idx + 1):
                                return True
                            place(r, c, v, False)
            return False

        if solve_recursive(0):
            solved_count += 1

    print(solved_count)

if __name__ == '__main__':
    solve()
