"""
Problem: 3Sum (LeetCode #15)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Should the result contain duplicate triplets? (No, only unique triplets)
- Can elements repeat in the input? (Yes)
- Can we use the same element more than once in a triplet? (No)
- Is the result order important? (No)

APPROACH / PSEUDOCODE:
- Sort the array to enable two-pointer technique and easy duplicate skipping
- For each index i (fix one number):
    - Skip duplicates at i
    - Use two pointers (left = i+1, right = n-1) to find pairs summing to -nums[i]
    - If found: record triplet, skip duplicates for both pointers, continue
    - If sum < 0: move left pointer right
    - If sum > 0: move right pointer left

Time Complexity: O(n^2) - outer loop O(n) × two pointer O(n)
Space Complexity: O(1) excluding output (sorting is in-place)
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate values for the fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# Test cases
if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(threeSum([0, 1, 1]))               # []
    print(threeSum([0, 0, 0]))               # [[0,0,0]]
