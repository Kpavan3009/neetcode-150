"""
Problem: Longest Common Subsequence (LeetCode #1143)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Subsequence (not substring) - characters don't need to be contiguous? (Yes)
- Return length of LCS? (Yes)
- Strings can be empty? (Yes, LCS = 0)

APPROACH / PSEUDOCODE:
- dp[i][j] = LCS of text1[0..i-1] and text2[0..j-1]
- If text1[i-1] == text2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
- Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- Space optimize to 2 rows

Time Complexity: O(m * n)
Space Complexity: O(min(m, n)) - two row arrays
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    # Ensure text2 is shorter for space optimization
    if m < n:
        text1, text2 = text2, text1
        m, n = n, m

    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr, [0] * (n + 1)

    return prev[n]


# Test cases
if __name__ == "__main__":
    print(longestCommonSubsequence("abcde", "ace"))   # 3 ("ace")
    print(longestCommonSubsequence("abc", "abc"))     # 3
    print(longestCommonSubsequence("abc", "def"))     # 0
