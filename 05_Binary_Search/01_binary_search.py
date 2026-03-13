"""
Problem: Binary Search (LeetCode #704)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Is the array sorted? (Yes, sorted in ascending order)
- Can there be duplicates? (No, all elements are unique)
- Return -1 if not found? (Yes)

APPROACH / PSEUDOCODE:
- Classic binary search with two pointers: left=0, right=n-1
- Compute mid = left + (right - left) // 2 (avoids integer overflow)
- If nums[mid] == target → return mid
- If nums[mid] < target → search right half (left = mid + 1)
- If nums[mid] > target → search left half (right = mid - 1)
- Return -1 if not found

Time Complexity: O(log n) - halve search space each iteration
Space Complexity: O(1)
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test cases
if __name__ == "__main__":
    print(search([-1,0,3,5,9,12], 9))   # 4
    print(search([-1,0,3,5,9,12], 2))   # -1
