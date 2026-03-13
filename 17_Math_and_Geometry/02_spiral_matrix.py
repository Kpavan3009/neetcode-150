"""
Problem: Spiral Matrix (LeetCode #54)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Traverse in spiral order (clockwise from top-left)? (Yes)
- Can be non-square matrix? (Yes, m x n)
- Can be empty? (Yes, return [])

APPROACH / PSEUDOCODE:
- Use four boundaries: top, bottom, left, right
- Traverse: right along top, down along right, left along bottom, up along left
- After each traversal, shrink the corresponding boundary
- Continue while top <= bottom and left <= right

Time Complexity: O(m * n)
Space Complexity: O(1) excluding output
"""

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse right
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # Traverse down
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        # Traverse left
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        # Traverse up
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result


# Test cases
if __name__ == "__main__":
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))          # [1,2,3,6,9,8,7,4,5]
    print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
