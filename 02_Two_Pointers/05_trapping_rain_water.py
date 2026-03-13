"""
Problem: Trapping Rain Water (LeetCode #42)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Can the array be empty or have fewer than 3 elements? (Yes, return 0)
- Can heights be zero? (Yes)
- Are heights always non-negative integers? (Yes)

APPROACH / PSEUDOCODE:
- For each position, water trapped = min(max_left, max_right) - height[i]
- Two-pointer approach:
    - Maintain left_max and right_max running maximums
    - Start with left=0, right=n-1 pointers
    - If left_max <= right_max: process left side (water = left_max - height[left])
      because right side is guaranteed to be >= left_max
    - Else: process right side (water = right_max - height[right])
    - Move corresponding pointer inward

Time Complexity: O(n) - single pass
Space Complexity: O(1) - only pointer and max variables
"""

from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


# Test cases
if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(trap([4, 2, 0, 3, 2, 5]))                      # 9
    print(trap([]))                                        # 0
