"""
Problem: Combination Sum (LeetCode #39)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can we use the same number multiple times? (Yes)
- All numbers are positive? (Yes)
- No duplicate combinations in output? (Correct, sort and don't go back)

APPROACH / PSEUDOCODE:
- Backtracking: at each step pick a number (can reuse same index)
- Subtract from remaining target; if 0 → found combination
- If target < 0 → prune
- Iterate from current index to avoid duplicates

Time Complexity: O(2^(target/min_candidate)) - exponential
Space Complexity: O(target/min_candidate) - recursion depth
"""

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(start: int, current: List[int], remaining: int) -> None:
        if remaining == 0:
            result.append(list(current))
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i not i+1 (can reuse)
            current.pop()

    backtrack(0, [], target)
    return result


# Test cases
if __name__ == "__main__":
    print(combinationSum([2,3,6,7], 7))  # [[2,2,3],[7]]
    print(combinationSum([2,3,5], 8))    # [[2,2,2,2],[2,3,3],[3,5]]
