"""
Problem: Word Break (LeetCode #139)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can reuse words from dictionary? (Yes)
- s can be composed of multiple words? (Yes)
- Word dictionary has no duplicates? (Yes, but doesn't matter)

APPROACH / PSEUDOCODE:
- dp[i] = True if s[0..i-1] can be segmented using wordDict
- dp[0] = True (empty string)
- For each i from 1 to n:
    For each j from 0 to i:
        if dp[j] and s[j:i] in word_set → dp[i] = True
- Return dp[n]

Time Complexity: O(n^2 * m) where m = avg word length for substring check
Space Complexity: O(n + |dict|)
"""

from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # optimization: no need to check more j values

    return dp[n]


# Test cases
if __name__ == "__main__":
    print(wordBreak("leetcode", ["leet","code"]))           # True
    print(wordBreak("applepenapple", ["apple","pen"]))       # True
    print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # False
