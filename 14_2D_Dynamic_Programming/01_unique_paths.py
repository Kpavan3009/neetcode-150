"""
Problem: Unique Paths (LeetCode #62)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can only move right or down? (Yes)
- Grid is m x n? (Yes)
- Start at top-left, end at bottom-right? (Yes)

APPROACH / PSEUDOCODE:
- dp[i][j] = number of unique paths to reach cell (i,j)
- Base case: first row and first column all have 1 path
- dp[i][j] = dp[i-1][j] + dp[i][j-1]
- Optimize to 1D array

Time Complexity: O(m * n)
Space Complexity: O(n) - 1D DP array
"""


def uniquePaths(m: int, n: int) -> int:
    dp = [1] * n  # first row is all 1s

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]  # dp[j] = from above; dp[j-1] = from left

    return dp[n - 1]


# Math approach: C(m+n-2, m-1) - O(1) with large number math
from math import comb
def uniquePaths_math(m: int, n: int) -> int:
    return comb(m + n - 2, m - 1)


# Test cases
if __name__ == "__main__":
    print(uniquePaths(3, 7))  # 28
    print(uniquePaths(3, 2))  # 3
