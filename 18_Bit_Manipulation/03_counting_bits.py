"""
Problem: Counting Bits (LeetCode #338)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Return array where ans[i] = number of 1s in binary representation of i? (Yes)
- For all i in [0, n]? (Yes)

APPROACH / PSEUDOCODE:
- DP approach: dp[i] = dp[i >> 1] + (i & 1)
  - dp[i] = bits in i//2 (same bits, just right-shifted) + last bit of i
- This achieves O(n) without any individual bit counting

Time Complexity: O(n)
Space Complexity: O(n) - output array
"""

from typing import List


def countBits(n: int) -> List[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


# Test cases
if __name__ == "__main__":
    print(countBits(2))  # [0,1,1]
    print(countBits(5))  # [0,1,1,2,1,2]
