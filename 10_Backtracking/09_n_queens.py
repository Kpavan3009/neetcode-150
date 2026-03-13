"""
Problem: N-Queens (LeetCode #51)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Return all distinct solutions? (Yes)
- n is always >= 1? (Yes)
- Queens attack in same row, column, diagonal? (Yes)

APPROACH / PSEUDOCODE:
- Place queens row by row
- Track which columns and diagonals (both directions) are under attack
- For each row, try placing queen in each column:
    - If column, pos_diag (row-col), neg_diag (row+col) all free → place queen
    - Recurse to next row
    - Backtrack: remove queen, free column and diagonals

Time Complexity: O(n!) - at most n choices for row 1, n-1 for row 2, etc.
Space Complexity: O(n^2) - board representation
"""

from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    result = []
    cols = set()
    pos_diag = set()  # row - col
    neg_diag = set()  # row + col
    board = [['.' ] * n for _ in range(n)]

    def backtrack(row: int) -> None:
        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row - col) in pos_diag or (row + col) in neg_diag:
                continue

            cols.add(col)
            pos_diag.add(row - col)
            neg_diag.add(row + col)
            board[row][col] = 'Q'

            backtrack(row + 1)

            cols.remove(col)
            pos_diag.remove(row - col)
            neg_diag.remove(row + col)
            board[row][col] = '.'

    backtrack(0)
    return result


# Test cases
if __name__ == "__main__":
    solutions = solveNQueens(4)
    print(f"Number of solutions for n=4: {len(solutions)}")  # 2
    for sol in solutions:
        for row in sol:
            print(row)
        print()
