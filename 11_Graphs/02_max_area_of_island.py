"""
Problem: Max Area of Island (LeetCode #695)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Area = number of connected 1-cells? (Yes, 4-directional connectivity)
- Return 0 if no island? (Yes)
- Can modify grid? (Yes)

APPROACH / PSEUDOCODE:
- Same DFS approach as Number of Islands
- DFS returns the area of current island (count cells visited)
- Track and return maximum area found

Time Complexity: O(m * n)
Space Complexity: O(m * n) - recursion
"""

from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0  # mark visited
        return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))

    return max_area


# Test cases
if __name__ == "__main__":
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    print(maxAreaOfIsland(grid))  # 6
