"""
Problem: Subsets (LeetCode #78)
Difficulty: Medium

CLARIFYING QUESTIONS:
- All elements are unique? (Yes)
- Include the empty set? (Yes)
- Any order for output? (No)

APPROACH / PSEUDOCODE:
- Backtracking: at each index, decide to include or exclude current element
- Start with empty subset, recurse with next index
- Add current state to result at every call (not just at leaf)

Time Complexity: O(n * 2^n) - 2^n subsets, each takes O(n) to copy
Space Complexity: O(n) recursion depth
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(start: int, current: List[int]) -> None:
        result.append(list(current))  # add current subset

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()  # undo choice

    backtrack(0, [])
    return result


# Test cases
if __name__ == "__main__":
    print(subsets([1,2,3]))
    # [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
    print(subsets([0]))  # [[], [0]]
