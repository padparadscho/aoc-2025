with open('07/input.txt', 'r') as f:
    lines = f.read().splitlines()


def solve_part_1(lines):
    grid = lines
    height = len(grid)
    width = len(grid[0])

    # Find S
    start_row = -1
    start_col = -1
    for r, line in enumerate(grid):
        if 'S' in line:
            start_row = r
            start_col = line.find('S')
            break
            
    if start_row == -1:
        print("Start point S not found")
        return

    active_cols = {start_col}
    total_splits = 0

    # Simulate beam propagation row by row
    # Start checking from the row BELOW S, because the beam moves downward from S
    for r in range(start_row + 1, height):
        next_active_cols = set()
        
        if not active_cols:
            break
            
        for c in active_cols:
            # Check if beam is within horizontal bounds
            if 0 <= c < width:
                char = grid[r][c]
                
                if char == '^':
                    total_splits += 1
                    # Split: create beams at left and right
                    # These new beams will be processed in the NEXT row
                    next_active_cols.add(c - 1)
                    next_active_cols.add(c + 1)
                else:
                    # Beam continues straight down
                    next_active_cols.add(c)
            else:
                # Beam exited the manifold horizontally (though usually they exit at the bottom)
                pass
                
        active_cols = next_active_cols

    print(f"Part 1 Solution: {total_splits}")


def solve_part_2(lines):
    grid = lines
    height = len(grid)
    width = len(grid[0])

    # Find S
    start_row = -1
    start_col = -1
    for r, line in enumerate(grid):
        if 'S' in line:
            start_row = r
            start_col = line.find('S')
            break
            
    if start_row == -1:
        print("Start point S not found")
        return

    # Map of (row, col) -> number of timelines reaching this point
    # Start with 1 timeline at S
    active_points = {start_col: 1}

    # Simulate beam propagation row by row
    for r in range(start_row + 1, height):
        next_active_points = {}
        
        if not active_points:
            break
            
        for c, count in active_points.items():
            # Check if beam is within horizontal bounds
            if 0 <= c < width:
                char = grid[r][c]
                
                if char == '^':
                    # Split: create beams at left and right
                    # Each split creates two new timelines for EACH incoming timeline
                    # Left path
                    next_active_points[c - 1] = next_active_points.get(c - 1, 0) + count
                    # Right path
                    next_active_points[c + 1] = next_active_points.get(c + 1, 0) + count
                else:
                    # Beam continues straight down
                    # Number of timelines is preserved
                    next_active_points[c] = next_active_points.get(c, 0) + count
            else:
                # Beam exited the manifold horizontally
                pass
                
        active_points = next_active_points

    total_timelines = sum(active_points.values())
    print(f"Part 2 Solution: {total_timelines}")


if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)
