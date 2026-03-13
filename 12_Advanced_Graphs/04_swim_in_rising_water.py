"""
Problem: Swim in Rising Water (LeetCode #778)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Grid[i][j] = elevation at that cell? (Yes)
- Can swim when water level >= current cell elevation? (Yes)
- Move to 4-adjacent cells at same time step? (Yes)
- Minimize time to reach (n-1, n-1) from (0,0)? (Yes)

APPROACH / PSEUDOCODE:
- Modified Dijkstra: instead of minimizing sum, minimize the maximum elevation visited
- Min-heap: (max_elevation_so_far, row, col)
- At each step, pick cell with lowest max elevation to reach it
- When we reach (n-1, n-1) → that's the answer

Time Complexity: O(n^2 log n)
Space Complexity: O(n^2)
"""

import heapq
from typing import List


def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    visited = set()
    heap = [(grid[0][0], 0, 0)]  # (max_elevation, row, col)

    while heap:
        t, r, c = heapq.heappop(heap)

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if r == n - 1 and c == n - 1:
            return t

        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))

    return -1


# Test cases
if __name__ == "__main__":
    print(swimInWater([[0,2],[1,3]]))  # 3
    print(swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))  # 16
