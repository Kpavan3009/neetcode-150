"""
Problem: Number of Islands (LeetCode #200)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Connected in 4 directions (not diagonal)? (Yes)
- Can modify the grid? (Yes, we can mark visited cells)
- Can grid be empty? (Yes, return 0)

APPROACH / PSEUDOCODE:
- Iterate every cell; when we find a '1', increment count and BFS/DFS to mark entire island
- DFS: mark current cell as '0' (visited), recurse on 4 neighbors that are '1'
- Each DFS call explores and marks one complete island

Time Complexity: O(m * n)
Space Complexity: O(m * n) - recursion stack in worst case
"""

from typing import List


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # mark visited
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count


# Test cases
if __name__ == "__main__":
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(grid1))  # 1

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(grid2))  # 3
