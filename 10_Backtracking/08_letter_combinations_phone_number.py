"""
Problem: Letter Combinations of a Phone Number (LeetCode #17)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Empty input → return []? (Yes)
- Only digits 2-9 in input? (Yes)
- Return all possible combinations? (Yes, in any order)

APPROACH / PSEUDOCODE:
- Map each digit to its letters (like a phone keypad)
- Backtracking: for each digit, try each mapped letter
- When current combination length == input length → add to result

Time Complexity: O(4^n * n) where n = input length (4 for digits like 7, 9)
Space Complexity: O(n) recursion depth
"""

from typing import List


def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    result = []

    def backtrack(idx: int, current: str) -> None:
        if idx == len(digits):
            result.append(current)
            return

        for ch in phone_map[digits[idx]]:
            backtrack(idx + 1, current + ch)

    backtrack(0, "")
    return result


# Test cases
if __name__ == "__main__":
    print(letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(letterCombinations(""))    # []
    print(letterCombinations("2"))   # ["a","b","c"]
