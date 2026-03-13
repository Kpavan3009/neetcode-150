"""
Problem: Generate Parentheses (LeetCode #22)
Difficulty: Medium

CLARIFYING QUESTIONS:
- n is the number of pairs of parentheses? (Yes)
- Should all combinations be returned? (Yes, all well-formed combinations)
- Is n always positive? (Yes, n >= 1)

APPROACH / PSEUDOCODE:
- Backtracking / recursion with a stack/string builder
- At each step, we can:
    - Add '(' if open count < n
    - Add ')' if close count < open count
- Base case: when string length == 2*n, add to result
- This naturally generates all valid combinations

Time Complexity: O(4^n / sqrt(n)) - Catalan number (number of valid combinations)
Space Complexity: O(n) - recursion depth
"""

from typing import List


def generateParenthesis(n: int) -> List[str]:
    result = []

    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# Test cases
if __name__ == "__main__":
    print(generateParenthesis(3))
    # ["((()))","(()())","(())()","()(())","()()()"]
    print(generateParenthesis(1))  # ["()"]
