with open('03/input.txt', 'r') as f:
    lines = f.readlines()


def solve_part_1(lines):
    total_joltage = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        max_joltage = -1
        
        # We need to find two digits d1 (at index i) and d2 (at index j)
        # such that i < j and d1 * 10 + d2 is maximized.
        
        # Optimization: We want d1 to be as large as possible.
        # We can iterate d1 from 9 down to 1.
        # The first time we find a d1 that allows a valid d2, we might not be done
        # because a slightly smaller d1 might be followed by a 9, while the larger d1 is followed by a 0.
        # Given the small line length, O(N^2) is perfectly fine and safer.
        
        digits = [int(c) for c in line if c.isdigit()]
        n = len(digits)
        
        for i in range(n):
            for j in range(i + 1, n):
                val = digits[i] * 10 + digits[j]
                if val > max_joltage:
                    max_joltage = val
        
        if max_joltage != -1:
            total_joltage += max_joltage

    print(f"Part 1 Solution: {total_joltage}")


def solve_part_2(lines):
    total_joltage = 0
    REQUIRED_LENGTH = 12

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        digits = [int(c) for c in line if c.isdigit()]
        n = len(digits)
        
        if n < REQUIRED_LENGTH:
            # Should not happen based on problem description, but good to handle
            continue
            
        current_pos = -1
        result_digits = []
        
        # We need to pick REQUIRED_LENGTH digits
        for i in range(REQUIRED_LENGTH):
            digits_needed_after_this = REQUIRED_LENGTH - 1 - i
            
            # The range of valid indices for the next digit:
            # Start: just after the last picked digit
            # End: must leave enough digits for the rest
            start_index = current_pos + 1
            end_index = n - digits_needed_after_this # Exclusive for range/slice
            
            # Find the largest digit in the valid window
            # We want the first occurrence of the largest digit to maximize remaining options
            window = digits[start_index : end_index]
            
            max_digit = -1
            best_idx_in_window = -1
            
            for idx, digit in enumerate(window):
                if digit > max_digit:
                    max_digit = digit
                    best_idx_in_window = idx
                if digit == 9:
                    # Optimization: 9 is the max possible digit, so we can stop early
                    # if we find a 9, since we want the first occurrence.
                    break
            
            result_digits.append(str(max_digit))
            current_pos = start_index + best_idx_in_window
            
        total_joltage += int("".join(result_digits))

    print(f"Part 2 Solution: {total_joltage}")


if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)

