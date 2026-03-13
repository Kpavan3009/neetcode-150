"""
Problem: Walls and Gates (LeetCode #286 / NeetCode)
Difficulty: Medium

CLARIFYING QUESTIONS:
- INF = 2^31 - 1 represents empty rooms? (Yes)
- -1 = walls (impassable)? (Yes)
- 0 = gates? (Yes)
- Fill each empty room with distance to nearest gate? (Yes)

APPROACH / PSEUDOCODE:
- Multi-source BFS starting from ALL gates simultaneously
- Initialize queue with all gate positions (value = 0)
- BFS outward: each neighbor that is INF gets distance = current + 1
- BFS guarantees shortest distance for each cell

Time Complexity: O(m * n) - each cell processed once
Space Complexity: O(m * n) - queue
"""

from collections import deque
from typing import List


def wallsAndGates(rooms: List[List[int]]) -> None:
    INF = 2**31 - 1
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()

    # Initialize with all gates
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))


# Test cases
if __name__ == "__main__":
    INF = 2**31 - 1
    rooms = [
        [INF, -1,  0, INF],
        [INF, INF, INF, -1],
        [INF, -1,  INF, -1],
        [0,  -1,  INF, INF]
    ]
    wallsAndGates(rooms)
    for row in rooms:
        print(row)
    # [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
