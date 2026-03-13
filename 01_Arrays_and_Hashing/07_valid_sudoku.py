"""
Problem: Valid Sudoku (LeetCode #36)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Do I need to solve the sudoku or just validate it? (Just validate)
- Empty cells are represented as '.'? (Yes)
- Is the board always 9x9? (Yes)
- Should I validate that a solution exists, or just that current state has no conflicts? (No conflicts)

APPROACH / PSEUDOCODE:
- Use three sets of hash sets: one for rows, one for columns, one for 3x3 boxes
- For each cell (i, j) with a digit:
    - Check if digit already in row i → invalid
    - Check if digit already in col j → invalid
    - Check if digit already in box (i//3, j//3) → invalid
    - Otherwise add to all three sets
- Return True if no conflicts found

Time Complexity: O(1) - board is always 9x9 = 81 cells
Space Complexity: O(1) - at most 9 values per row/col/box (bounded by board size)
"""

from typing import List
from collections import defaultdict


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == '.':
                continue

            box_key = (i // 3, j // 3)

            if val in rows[i] or val in cols[j] or val in boxes[box_key]:
                return False

            rows[i].add(val)
            cols[j].add(val)
            boxes[box_key].add(val)

    return True


# Test cases
if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(isValidSudoku(board))  # True
