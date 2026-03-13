"""
Problem: Interleaving String (LeetCode #97)
Difficulty: Medium

CLARIFYING QUESTIONS:
- s3 is interleaving if formed by interleaving characters of s1 and s2? (Yes)
- Order within s1 and s2 must be maintained? (Yes)
- Lengths: len(s1) + len(s2) == len(s3)? (Yes, else False)

APPROACH / PSEUDOCODE:
- dp[i][j] = can s3[0..i+j-1] be formed by interleaving s1[0..i-1] and s2[0..j-1]
- dp[i][j] = True if:
    (dp[i-1][j] and s1[i-1] == s3[i+j-1]) OR
    (dp[i][j-1] and s2[j-1] == s3[i+j-1])
- Space optimize to 1D

Time Complexity: O(m * n)
Space Complexity: O(n)
"""


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False

    dp = [False] * (n + 1)
    dp[0] = True

    # Initialize first row (using only s2)
    for j in range(1, n + 1):
        dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

    for i in range(1, m + 1):
        # Update dp[0] for using only s1
        dp[0] = dp[0] and s1[i-1] == s3[i-1]
        for j in range(1, n + 1):
            dp[j] = ((dp[j] and s1[i-1] == s3[i+j-1]) or
                     (dp[j-1] and s2[j-1] == s3[i+j-1]))

    return dp[n]


# Test cases
if __name__ == "__main__":
    print(isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
    print(isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # False
    print(isInterleave("", "", ""))                       # True
