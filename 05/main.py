with open('05/input.txt', 'r') as f:
    content = f.read()


def solve_part_1(content):
    # Split input into ranges and IDs based on the blank line
    parts = content.strip().split('\n\n')
    ranges_part = parts[0].splitlines()
    ids_part = parts[1].splitlines()

    # Parse ranges
    ranges = []
    for line in ranges_part:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    # Parse IDs
    ids = [int(line) for line in ids_part]

    fresh_count = 0
    for ingredient_id in ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1

    print(f"Part 1 Solution: {fresh_count}")


def solve_part_2(content):
    # Split input into ranges and IDs based on the blank line
    parts = content.strip().split('\n\n')
    ranges_part = parts[0].splitlines()

    # Parse ranges
    ranges = []
    for line in ranges_part:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    # Sort ranges by start value
    ranges.sort(key=lambda x: x[0])

    merged_ranges = []
    if ranges:
        current_start, current_end = ranges[0]
        
        for i in range(1, len(ranges)):
            next_start, next_end = ranges[i]
            
            if next_start <= current_end + 1: # Overlapping or adjacent
                current_end = max(current_end, next_end)
            else:
                merged_ranges.append((current_start, current_end))
                current_start, current_end = next_start, next_end
        
        merged_ranges.append((current_start, current_end))

    total_fresh_ids = 0
    for start, end in merged_ranges:
        total_fresh_ids += (end - start + 1)

    print(f"Part 2 Solution: {total_fresh_ids}")


if __name__ == "__main__":
    solve_part_1(content)
    solve_part_2(content)