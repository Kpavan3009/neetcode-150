"""
Problem: Palindrome Partitioning (LeetCode #131)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Every substring in a partition must be a palindrome? (Yes)
- Return all possible partitionings? (Yes)
- Can single characters be palindromes? (Yes)

APPROACH / PSEUDOCODE:
- Backtracking: at each position, try all substrings starting here
- If substring is palindrome → add to current partition, recurse
- When we reach end of string → add current partition to results
- Backtrack by removing last added substring

Time Complexity: O(n * 2^n) - 2^n partitions, palindrome check O(n)
Space Complexity: O(n) depth
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    result = []

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def backtrack(start: int, current: List[str]) -> None:
        if start == len(s):
            result.append(list(current))
            return

        for end in range(start + 1, len(s) + 1):
            substr = s[start:end]
            if is_palindrome(substr):
                current.append(substr)
                backtrack(end, current)
                current.pop()

    backtrack(0, [])
    return result


# Test cases
if __name__ == "__main__":
    print(partition("aab"))  # [["a","a","b"],["aa","b"]]
    print(partition("a"))    # [["a"]]
