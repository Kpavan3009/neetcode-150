"""
Problem: Longest Increasing Path in a Matrix (LeetCode #329)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Move in 4 directions? (Yes)
- Strictly increasing? (Yes)
- Can revisit cells? (No, strictly increasing prevents cycles)

APPROACH / PSEUDOCODE:
- DFS + memoization
- For each cell, compute longest increasing path starting from it
- Cache result to avoid recomputation
- No visited set needed (strictly increasing prevents revisiting)

Time Complexity: O(m * n)
Space Complexity: O(m * n) - memoization cache
"""

from typing import List
from functools import lru_cache


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])

    @lru_cache(maxsize=None)
    def dfs(r: int, c: int) -> int:
        best = 1
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))
        return best

    return max(dfs(r, c) for r in range(rows) for c in range(cols))


# Test cases
if __name__ == "__main__":
    print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # 4 [1,2,6,9]
    print(longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))  # 4 [3,4,5,6]
