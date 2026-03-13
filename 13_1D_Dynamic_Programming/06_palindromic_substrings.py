"""
Problem: Palindromic Substrings (LeetCode #647)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Count ALL palindromic substrings (including single characters)? (Yes)
- Single characters count as palindromes? (Yes)
- Overlapping substrings counted separately? (Yes)

APPROACH / PSEUDOCODE:
- Expand around each center (same as Longest Palindromic Substring)
- For each valid expansion, increment count
- O(n^2) time, O(1) space

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def countSubstrings(s: str) -> int:
    count = 0

    def expand(left: int, right: int) -> None:
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)      # Odd length
        expand(i, i + 1)  # Even length

    return count


# Test cases
if __name__ == "__main__":
    print(countSubstrings("abc"))   # 3 (a, b, c)
    print(countSubstrings("aaa"))   # 6 (a, a, a, aa, aa, aaa)
