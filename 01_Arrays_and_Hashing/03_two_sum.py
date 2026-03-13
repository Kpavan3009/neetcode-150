"""
Problem: Two Sum (LeetCode #1)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Is there always exactly one valid answer? (Yes, guaranteed)
- Can I use the same element twice? (No)
- Can the array have duplicates? (Yes)
- Should I return indices or values? (Indices)
- Is the array sorted? (No, not necessarily)

APPROACH / PSEUDOCODE:
- Use a hash map to store {value: index} as we iterate
- For each number, compute its complement = target - num
- If complement exists in map → found pair, return [map[complement], i]
- Otherwise store current number and its index in map
- Single pass, no nested loops needed

Time Complexity: O(n) - single pass
Space Complexity: O(n) - hash map stores up to n elements
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # guaranteed to have a solution per problem statement


# Test cases
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(twoSum([3, 2, 4], 6))        # [1, 2]
    print(twoSum([3, 3], 6))           # [0, 1]
