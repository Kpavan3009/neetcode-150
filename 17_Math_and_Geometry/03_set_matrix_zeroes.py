"""
Problem: Set Matrix Zeroes (LeetCode #73)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Set entire row and column to 0 if a cell is 0? (Yes)
- Do it in place? (Yes)
- Need to track which cells were originally 0 (not set to 0 later)? (Yes)

APPROACH / PSEUDOCODE:
- Use first row and first column as markers
- First check if first row/column themselves contain zeros (save in flags)
- Mark: for each 0 found in rest of matrix, set matrix[0][c] and matrix[r][0] to 0
- Apply markers: set rows/cols to 0 based on first row/col markers
- Finally, handle first row and column based on saved flags

Time Complexity: O(m * n)
Space Complexity: O(1) - using matrix itself as markers
"""

from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Use first row and col as markers for the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # Zero out rows and columns based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    # Handle first row and column
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


# Test cases
if __name__ == "__main__":
    m1 = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(m1)
    print(m1)  # [[1,0,1],[0,0,0],[1,0,1]]

    m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setZeroes(m2)
    print(m2)  # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
