"""
Problem: Sum of Two Integers (LeetCode #371)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Add without using + or - operators? (Yes)
- Handle negative numbers? (Yes)
- 32-bit integers? (Yes)

APPROACH / PSEUDOCODE:
- XOR gives sum without carry: a XOR b
- AND gives carry positions: (a AND b) << 1
- Repeat until no carry (carry = 0)
- Python integers are unbounded → need to mask to 32-bit

Time Complexity: O(1) - at most 32 iterations
Space Complexity: O(1)
"""


def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF  # 32-bit mask
    MAX = 0x7FFFFFFF   # max positive 32-bit int

    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & MASK   # XOR and mask to 32 bits
        b = carry & MASK

    # If a > MAX, it's a negative number in two's complement
    return a if a <= MAX else ~(a ^ MASK)


# Test cases
if __name__ == "__main__":
    print(getSum(1, 2))    # 3
    print(getSum(2, 3))    # 5
    print(getSum(-1, 1))   # 0
    print(getSum(-2, -3))  # -5
