"""
Problem: Find Minimum in Rotated Sorted Array (LeetCode #153)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Are all values unique? (Yes)
- Can the array be non-rotated (already sorted)? (Yes)
- Array always non-empty? (Yes)

APPROACH / PSEUDOCODE:
- Binary search: the minimum is the inflection point
- If nums[mid] > nums[right] → minimum is in right half (left = mid + 1)
  (mid is in the larger left portion of rotation)
- Else → minimum is in left half including mid (right = mid)
- When left == right, we've found the minimum

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1  # min is in right half
        else:
            right = mid     # min is in left half (including mid)

    return nums[left]


# Test cases
if __name__ == "__main__":
    print(findMin([3,4,5,1,2]))    # 1
    print(findMin([4,5,6,7,0,1,2]))  # 0
    print(findMin([11,13,15,17]))  # 11 (not rotated)
