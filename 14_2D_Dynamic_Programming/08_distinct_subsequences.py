"""
Problem: Distinct Subsequences (LeetCode #115)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Count distinct subsequences of s equal to t? (Yes)
- Each subsequence uses different indices? (Yes)
- Can be very large (just return the count, no modulo)? (Yes)

APPROACH / PSEUDOCODE:
- dp[i][j] = number of ways to form t[0..j-1] from s[0..i-1]
- If s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
  (use this s[i-1] to match, OR skip s[i-1])
- Else: dp[i][j] = dp[i-1][j] (skip s[i-1])
- Space optimize to 1D (process backwards)

Time Complexity: O(m * n)
Space Complexity: O(n)
"""


def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1  # empty t is a subsequence of any s

    for i in range(1, m + 1):
        for j in range(n, 0, -1):  # backwards to avoid using s[i] twice
            if s[i-1] == t[j-1]:
                dp[j] += dp[j-1]

    return dp[n]


# Test cases
if __name__ == "__main__":
    print(numDistinct("rabbbit", "rabbit"))  # 3
    print(numDistinct("babgbag", "bag"))     # 5
