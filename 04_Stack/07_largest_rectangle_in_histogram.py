"""
Problem: Largest Rectangle in Histogram (LeetCode #84)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Can heights be 0? (Yes)
- Can the array be empty? (No, at least 1 bar)
- Are heights always non-negative integers? (Yes)

APPROACH / PSEUDOCODE:
- Use a monotonic increasing stack of (index, height)
- For each bar:
    - While stack non-empty and current height < stack top height:
        - Pop (idx, h) from stack
        - Width extends from idx to current position - 1
        - Area = h * (current_i - idx), update max
        - Set start = idx (current bar can extend back to where we popped)
    - Push (start, height) to stack
- After loop, process remaining bars in stack (extend to end)

Time Complexity: O(n) - each bar pushed/popped once
Space Complexity: O(n) - stack
"""

from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    stack = []  # (start_index, height)
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx  # extend start back to where we popped
        stack.append((start, h))

    # Process remaining bars (they extend to end of array)
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))

    return max_area


# Test cases
if __name__ == "__main__":
    print(largestRectangleArea([2,1,5,6,2,3]))  # 10
    print(largestRectangleArea([2,4]))            # 4
    print(largestRectangleArea([1]))              # 1
