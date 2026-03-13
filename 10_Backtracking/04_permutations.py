"""
Problem: Permutations (LeetCode #46)
Difficulty: Medium

CLARIFYING QUESTIONS:
- All elements are unique? (Yes)
- Return all permutations? (Yes)
- Any order? (Yes)

APPROACH / PSEUDOCODE:
- Backtracking: use a boolean visited array
- At each step, pick any unvisited element, add to current permutation
- When current length == n → add to result
- Backtrack: unmark visited, remove from current

Time Complexity: O(n! * n) - n! permutations, each length n to copy
Space Complexity: O(n) recursion depth
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    used = [False] * len(nums)

    def backtrack(current: List[int]) -> None:
        if len(current) == len(nums):
            result.append(list(current))
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

    backtrack([])
    return result


# Test cases
if __name__ == "__main__":
    print(permute([1,2,3]))
    # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(permute([0,1]))   # [[0,1],[1,0]]
