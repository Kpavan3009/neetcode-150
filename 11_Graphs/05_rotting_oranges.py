"""
Problem: Rotting Oranges (LeetCode #994)
Difficulty: Medium

CLARIFYING QUESTIONS:
- 0 = empty, 1 = fresh, 2 = rotten? (Yes)
- Every minute, rotten orange spreads to 4-adjacent fresh oranges? (Yes)
- Return -1 if impossible? (Yes, if fresh oranges can't be reached)

APPROACH / PSEUDOCODE:
- Multi-source BFS from all initially rotten oranges
- Count fresh oranges initially
- BFS: spread rot each minute, decrement fresh count
- Return minutes elapsed; if fresh > 0 remaining → return -1

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    while queue:
        r, c, t = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                minutes = t + 1
                queue.append((nr, nc, t + 1))

    return minutes if fresh == 0 else -1


# Test cases
if __name__ == "__main__":
    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # 4
    print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1
    print(orangesRotting([[0,2]]))                     # 0
