"""
Problem: Reverse Integer (LeetCode #7)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Environment only stores 32-bit signed integers? (Yes)
- Return 0 if reversed integer overflows? (Yes)
- Negative numbers stay negative when reversed? (Yes)

APPROACH / PSEUDOCODE:
- Extract digits from right using % 10
- Build reversed number by multiplying by 10 each step
- Check for overflow before each step: if result > MAX_INT // 10 → overflow

Time Complexity: O(log n) - number of digits
Space Complexity: O(1)
"""


def reverse(x: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    sign = 1 if x >= 0 else -1
    x = abs(x)

    result = 0
    while x != 0:
        digit = x % 10
        x //= 10

        # Check overflow before updating result
        if result > (INT_MAX - digit) // 10:
            return 0

        result = result * 10 + digit

    result *= sign
    if result < INT_MIN or result > INT_MAX:
        return 0

    return result


# Test cases
if __name__ == "__main__":
    print(reverse(123))         # 321
    print(reverse(-123))        # -321
    print(reverse(120))         # 21
    print(reverse(1534236469))  # 0 (overflow)
