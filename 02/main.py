with open('02/input.txt', 'r') as f:
    lines = f.readlines()

content = "".join(lines).strip()
ranges_str = content.split(',')
ranges = []
for r_str in ranges_str:
    if r_str.strip():
        start_str, end_str = r_str.split('-')
        ranges.append((int(start_str), int(end_str)))


def is_invalid_id_part_1(n):
    s = str(n)
    length = len(s)
    
    # Must have even length to be two repeated sequences
    if length % 2 != 0:
        return False
    
    half = length // 2
    return s[:half] == s[half:]


def solve_part_1(ranges):
    total_invalid_sum = 0
    
    for start, end in ranges:
        # Iterate through the range [start, end] inclusive
        for num in range(start, end + 1):
            if is_invalid_id_part_1(num):
                total_invalid_sum += num
                
    print(f"Part 1 Solution: {total_invalid_sum}")


def is_invalid_id_part_2(n):
    s = str(n)
    length = len(s)
    
    # We look for a pattern length 'k' that divides 'length'
    # such that the string is the pattern repeated (length // k) times.
    # The pattern must be repeated at least twice, so k <= length // 2.
    for k in range(1, length // 2 + 1):
        if length % k == 0:
            pattern = s[:k]
            repetitions = length // k
            if pattern * repetitions == s:
                return True
    return False


def solve_part_2(ranges):
    total_invalid_sum = 0
    
    for start, end in ranges:
        # Iterate through the range [start, end] inclusive
        for num in range(start, end + 1):
            if is_invalid_id_part_2(num):
                total_invalid_sum += num
                
    print(f"Part 2 Solution: {total_invalid_sum}")


if __name__ == "__main__":
    solve_part_1(ranges)
    solve_part_2(ranges)
