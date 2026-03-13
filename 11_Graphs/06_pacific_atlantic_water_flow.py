"""
Problem: Pacific Atlantic Water Flow (LeetCode #417)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Water flows to neighbors with equal or lesser height? (Yes)
- Pacific = top and left edges; Atlantic = bottom and right edges? (Yes)
- Return cells that can reach BOTH oceans? (Yes)

APPROACH / PSEUDOCODE:
- Reverse approach: BFS from ocean edges inward (water flows uphill in reverse)
- BFS from all Pacific edge cells → mark cells reachable to Pacific
- BFS from all Atlantic edge cells → mark cells reachable to Atlantic
- Return intersection of both sets

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from collections import deque
from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    rows, cols = len(heights), len(heights[0])

    def bfs(starts) -> set:
        visited = set(starts)
        queue = deque(starts)
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return visited

    pacific_starts = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
    atlantic_starts = [(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)]

    pacific = bfs(pacific_starts)
    atlantic = bfs(atlantic_starts)

    return [[r, c] for r, c in pacific & atlantic]


# Test cases
if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(pacificAtlantic(heights))
    # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
