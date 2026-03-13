"""
Problem: Number of 1 Bits (LeetCode #191)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Count set bits (1s) in binary representation? (Yes)
- Unsigned 32-bit integer? (Yes)

APPROACH / PSEUDOCODE:
- Brian Kernighan's trick: n & (n-1) clears the lowest set bit
- Count how many times we can do this before n becomes 0

Time Complexity: O(number of set bits) ≤ O(32) = O(1)
Space Complexity: O(1)
"""


def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1  # clear lowest set bit
        count += 1
    return count


# Alternative: bit shift approach
def hammingWeight_shift(n: int) -> int:
    count = 0
    while n:
        count += n & 1  # check LSB
        n >>= 1
    return count


# Test cases
if __name__ == "__main__":
    print(hammingWeight(11))           # 3 (1011 has three 1s)
    print(hammingWeight(128))          # 1 (10000000)
    print(hammingWeight(2147483645))   # 30
