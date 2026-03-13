"""
Problem: Container With Most Water (LeetCode #11)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can the array contain zeros? (Yes)
- Is the array guaranteed to have at least 2 elements? (Yes)
- Do the lines have any width? (No, they're vertical lines of given height)
- Can heights be negative? (No, all non-negative)

APPROACH / PSEUDOCODE:
- Use two pointers: left at start, right at end
- Area = min(height[left], height[right]) * (right - left)
- The width decreases as we move pointers inward
- To potentially increase area, move the pointer with SMALLER height inward
  (moving the taller one can only decrease or maintain area)
- Track maximum area seen

Time Complexity: O(n) - single pass
Space Complexity: O(1)
"""

from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        water = min(height[left], height[right]) * width
        max_water = max(max_water, water)

        # Move the shorter line inward (greedy choice)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Test cases
if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(maxArea([1, 1]))                          # 1
