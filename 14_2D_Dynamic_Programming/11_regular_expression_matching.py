"""
Problem: Regular Expression Matching (LeetCode #10)
Difficulty: Hard

CLARIFYING QUESTIONS:
- '.' matches any single character? (Yes)
- '*' matches zero or more of the preceding element? (Yes)
- s contains only lowercase letters? (Yes)
- p contains lowercase letters, '.', and '*'? (Yes)

APPROACH / PSEUDOCODE:
- dp[i][j] = does p[0..j-1] match s[0..i-1]?
- Base: dp[0][0] = True; dp[0][j] = True if p[j-1]=='*' and dp[0][j-2]
- Transitions:
    If p[j-1] is letter or '.': dp[i][j] = dp[i-1][j-1] and (p[j-1]=='.' or p[j-1]==s[i-1])
    If p[j-1] == '*':
        Zero occurrences: dp[i][j] |= dp[i][j-2]
        One+ occurrences: dp[i][j] |= dp[i-1][j] and (p[j-2]=='.' or p[j-2]==s[i-1])

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Handle patterns like a* or a*b* that can match empty string
    for j in range(2, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-2]  # zero occurrences
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]

    return dp[m][n]


# Test cases
if __name__ == "__main__":
    print(isMatch("aa", "a"))    # False
    print(isMatch("aa", "a*"))   # True
    print(isMatch("ab", ".*"))   # True
    print(isMatch("aab", "c*a*b"))  # True
