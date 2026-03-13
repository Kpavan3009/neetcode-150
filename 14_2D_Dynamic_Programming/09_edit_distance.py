"""
Problem: Edit Distance (LeetCode #72)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Three operations: insert, delete, replace? (Yes)
- Minimize total operations to convert word1 to word2? (Yes)
- Can words be empty? (Yes)

APPROACH / PSEUDOCODE:
- dp[i][j] = min edit distance between word1[0..i-1] and word2[0..j-1]
- If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] (no edit needed)
- Else: dp[i][j] = 1 + min(dp[i-1][j],    ← delete from word1
                              dp[i][j-1],    ← insert into word1
                              dp[i-1][j-1])  ← replace

Time Complexity: O(m * n)
Space Complexity: O(min(m, n)) - two rows
"""


def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    # Space optimize: use two 1D arrays
    prev = list(range(n + 1))  # base case: deleting all of word2

    for i in range(1, m + 1):
        curr = [i] + [0] * n  # base case: deleting i chars from word1
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
        prev = curr

    return prev[n]


# Test cases
if __name__ == "__main__":
    print(minDistance("horse", "ros"))     # 3
    print(minDistance("intention", "execution"))  # 5
    print(minDistance("", "abc"))          # 3
