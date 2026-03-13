"""
Problem: Reverse Bits (LeetCode #190)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Reverse all 32 bits? (Yes, unsigned 32-bit integer)
- Result is also unsigned 32-bit? (Yes)

APPROACH / PSEUDOCODE:
- Build result bit by bit
- For each of 32 bits:
    - Shift result left by 1
    - OR with LSB of n
    - Shift n right by 1

Time Complexity: O(1) - always 32 iterations
Space Complexity: O(1)
"""


def reverseBits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


# Test cases
if __name__ == "__main__":
    # 43261596 = 00000010100101000001111010011100
    # reversed = 00111001011110000010100101000000 = 964176192
    print(reverseBits(43261596))  # 964176192

    # 4294967293 = 11111111111111111111111111111101
    # reversed = 10111111111111111111111111111111 = 3221225471
    print(reverseBits(4294967293))  # 3221225471
