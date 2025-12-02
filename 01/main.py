with open('01/input.txt', 'r') as f:
    lines = f.readlines()


def solve_part_1(lines):
    current_pos = 50
    zero_count = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        direction = line[0]
        distance = int(line[1:])

        if direction == 'L':
            current_pos = (current_pos - distance) % 100
        elif direction == 'R':
            current_pos = (current_pos + distance) % 100
        
        if current_pos == 0:
            zero_count += 1

    print(f"Part 1 Solution: {zero_count}")


def solve_part_2(lines):
    current_pos = 50
    total_zeros = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        direction = line[0]
        distance = int(line[1:])

        if direction == 'R':
            # Moving forward: count multiples of 100 in (current_pos, current_pos + distance]
            # Since current_pos < 100, floor(current_pos / 100) is 0.
            # So we just need floor((current_pos + distance) / 100)
            zeros = (current_pos + distance) // 100
            total_zeros += zeros
            current_pos = (current_pos + distance) % 100
        elif direction == 'L':
            # Moving backward: count multiples of 100 in [current_pos - distance, current_pos - 1]
            # Number of integers n such that current_pos - distance <= 100*n <= current_pos - 1
            # (current_pos - distance)/100 <= n <= (current_pos - 1)/100
            # n is in [ceil((current_pos - distance)/100), floor((current_pos - 1)/100)]
            
            floor_val = (current_pos - 1) // 100
            ceil_val = (current_pos - distance + 99) // 100
            zeros = floor_val - ceil_val + 1
            
            total_zeros += zeros
            current_pos = (current_pos - distance) % 100

    print(f"Part 2 Solution: {total_zeros}")


if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)