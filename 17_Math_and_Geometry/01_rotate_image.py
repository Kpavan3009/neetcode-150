"""
Problem: Rotate Image (LeetCode #48)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Rotate 90 degrees clockwise in place? (Yes)
- n x n matrix? (Yes)

APPROACH / PSEUDOCODE:
- Two steps:
    1. Transpose matrix (swap matrix[i][j] with matrix[j][i])
    2. Reverse each row
- After transpose + reverse each row = 90° clockwise rotation

Time Complexity: O(n^2)
Space Complexity: O(1) in-place
"""

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Step 1: Transpose (flip along main diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()


# Test cases
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    print(matrix)  # [[7,4,1],[8,5,2],[9,6,3]]

    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(matrix2)
    print(matrix2)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
