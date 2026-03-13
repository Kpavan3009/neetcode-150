"""
Problem: Surrounded Regions (LeetCode #130)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Capture = flip 'O' to 'X' if fully surrounded (not touching borders)? (Yes)
- 'O' connected to border cannot be captured? (Correct)
- 4-directional connectivity? (Yes)

APPROACH / PSEUDOCODE:
- Mark all 'O' cells connected to the border (they're safe) with 'T'
- Flip all remaining 'O' to 'X' (they're surrounded)
- Flip 'T' back to 'O'

Time Complexity: O(m * n)
Space Complexity: O(m * n) - recursion
"""

from typing import List


def solve(board: List[List[str]]) -> None:
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'T'  # temporary mark = safe
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

    # Mark border-connected 'O' cells as safe
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    # Flip surrounded 'O' to 'X', restore safe 'T' to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'T':
                board[r][c] = 'O'


# Test cases
if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    solve(board)
    for row in board:
        print(row)
    # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
