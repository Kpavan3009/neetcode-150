"""
Problem: Word Search (LeetCode #79)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can same cell be used more than once in a single path? (No)
- Word can start from any cell? (Yes)
- Only letters? (Yes)

APPROACH / PSEUDOCODE:
- DFS from each cell in grid
- At each step: check if current cell matches word[index]
- Mark cell as visited (use '#'), recurse in all 4 directions
- Restore cell after backtracking
- Return True if entire word matched

Time Complexity: O(m * n * 4^L) where L = word length
Space Complexity: O(L) recursion depth
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False

        temp = board[r][c]
        board[r][c] = '#'  # mark visited

        found = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))

        board[r][c] = temp  # restore
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False


# Test cases
if __name__ == "__main__":
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(exist(board1, "ABCCED"))  # True
    print(exist(board1, "SEE"))     # True
    print(exist(board1, "ABCB"))    # False
