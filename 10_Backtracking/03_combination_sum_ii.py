"""
Problem: Combination Sum II (LeetCode #40)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Each number can only be used once? (Yes)
- Can contain duplicates in input? (Yes)
- No duplicate combinations in output? (Correct)

APPROACH / PSEUDOCODE:
- Sort array to group duplicates together
- Backtracking: after using element at index i, start from i+1
- Skip duplicate elements at same recursion level:
    if i > start and candidates[i] == candidates[i-1] → skip

Time Complexity: O(2^n * n)
Space Complexity: O(n)
"""

from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    result = []

    def backtrack(start: int, current: List[int], remaining: int) -> None:
        if remaining == 0:
            result.append(list(current))
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # sorted, no point continuing

            # Skip duplicates at same level
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            current.append(candidates[i])
            backtrack(i + 1, current, remaining - candidates[i])
            current.pop()

    backtrack(0, [], target)
    return result


# Test cases
if __name__ == "__main__":
    print(combinationSum2([10,1,2,7,6,1,5], 8))  # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(combinationSum2([2,5,2,1,2], 5))         # [[1,2,2],[5]]
