"""
Problem: Search in Rotated Sorted Array (LeetCode #33)
Difficulty: Medium

CLARIFYING QUESTIONS:
- All values unique? (Yes)
- Return -1 if not found? (Yes)
- Can the array be non-rotated? (Yes)

APPROACH / PSEUDOCODE:
- Binary search with extra logic to determine which half is sorted
- At each step, one of the two halves is always sorted
- If left half is sorted (nums[left] <= nums[mid]):
    - If target is in [nums[left], nums[mid]) → search left
    - Else → search right
- Else right half is sorted (nums[mid] <= nums[right]):
    - If target is in (nums[mid], nums[right]] → search right
    - Else → search left

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Test cases
if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2], 0))   # 4
    print(search([4,5,6,7,0,1,2], 3))   # -1
    print(search([1], 0))               # -1
