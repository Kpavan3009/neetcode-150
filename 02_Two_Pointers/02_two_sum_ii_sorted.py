"""
Problem: Two Sum II - Input Array Is Sorted (LeetCode #167)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Is the array sorted in ascending order? (Yes)
- Is there always exactly one solution? (Yes)
- Can I use the same element twice? (No)
- Are indices 1-based or 0-based? (1-based per problem)
- Can there be negative numbers? (Yes)

APPROACH / PSEUDOCODE:
- Since array is sorted, use two pointers: left = 0, right = n-1
- Compute sum = nums[left] + nums[right]
- If sum == target → found it, return [left+1, right+1]
- If sum < target → need larger sum, move left pointer right
- If sum > target → need smaller sum, move right pointer left
- Guaranteed to find solution

Time Complexity: O(n) - single pass
Space Complexity: O(1) - only pointers
"""

from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]  # 1-indexed
        elif total < target:
            left += 1
        else:
            right -= 1

    return []  # guaranteed to have a solution


# Test cases
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))   # [1, 2]
    print(twoSum([2, 3, 4], 6))        # [1, 3]
    print(twoSum([-1, 0], -1))         # [1, 2]
