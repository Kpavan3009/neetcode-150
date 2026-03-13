"""
Problem: Longest Palindromic Substring (LeetCode #5)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Return the actual substring (not just length)? (Yes)
- Multiple palindromes of same length - return any? (Yes)
- Empty string? (Return "")

APPROACH / PSEUDOCODE:
- Expand around center for each possible center:
    - Odd-length palindromes: center at each character
    - Even-length palindromes: center between each pair of adjacent characters
- For each center, expand while characters match, track longest found

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def longestPalindrome(s: str) -> str:
    start, end = 0, 0

    def expand(left: int, right: int) -> None:
        nonlocal start, end
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > end - start:
                start, end = left, right
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)      # Odd length
        expand(i, i + 1)  # Even length

    return s[start:end + 1]


# Test cases
if __name__ == "__main__":
    print(longestPalindrome("babad"))   # "bab" or "aba"
    print(longestPalindrome("cbbd"))    # "bb"
    print(longestPalindrome("a"))       # "a"
    print(longestPalindrome("ac"))      # "a" or "c"
