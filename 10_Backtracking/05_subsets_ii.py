"""
Problem: Subsets II (LeetCode #90)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Array may contain duplicates? (Yes)
- No duplicate subsets in output? (Correct)

APPROACH / PSEUDOCODE:
- Sort array to group duplicates
- Backtracking same as Subsets I, but skip duplicate elements at same level
    if i > start and nums[i] == nums[i-1] → skip

Time Complexity: O(n * 2^n)
Space Complexity: O(n)
"""

from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    def backtrack(start: int, current: List[int]) -> None:
        result.append(list(current))

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # skip duplicate at same level

            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


# Test cases
if __name__ == "__main__":
    print(subsetsWithDup([1,2,2]))
    # [[],[1],[1,2],[1,2,2],[2],[2,2]]
    print(subsetsWithDup([0]))  # [[], [0]]
