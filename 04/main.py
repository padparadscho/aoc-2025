with open('04/input.txt', 'r') as f:
    lines = f.readlines()


def solve_part_1(lines):
    grid = [line.strip() for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    
    accessible_count = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                # Count adjacent rolls
                adjacent_rolls = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        
                        nr, nc = r + dr, c + dc
                        
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '@':
                                adjacent_rolls += 1
                
                if adjacent_rolls < 4:
                    accessible_count += 1

    print(f"Part 1 Solution: {accessible_count}")


def solve_part_2(lines):
    # Create a mutable grid
    grid = [list(line.strip()) for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    
    total_removed = 0
    
    while True:
        removed_in_this_round = 0
        to_remove = []
        
        # Identify rolls to remove
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    adjacent_rolls = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            
                            nr, nc = r + dr, c + dc
                            
                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == '@':
                                    adjacent_rolls += 1
                    
                    if adjacent_rolls < 4:
                        to_remove.append((r, c))
        
        if not to_remove:
            break
            
        # Remove them
        for r, c in to_remove:
            grid[r][c] = '.' # Or 'x', effectively not '@'
            removed_in_this_round += 1
            
        total_removed += removed_in_this_round
        
    print(f"Part 2 Solution: {total_removed}")


if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)