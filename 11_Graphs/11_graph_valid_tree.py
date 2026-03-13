"""
Problem: Graph Valid Tree (LeetCode #261 / NeetCode)
Difficulty: Medium

CLARIFYING QUESTIONS:
- A tree has n-1 edges and is fully connected with no cycles? (Yes)
- Undirected graph? (Yes)

APPROACH / PSEUDOCODE:
- A valid tree has exactly n-1 edges AND is connected (no cycle)
- Check 1: if len(edges) != n - 1 → not a tree (early exit)
- Check 2: use Union-Find; if any edge creates a cycle → not a tree
- Check 3: all nodes must be in same component

Time Complexity: O(n + E)
Space Complexity: O(n)
"""

from typing import List


def validTree(n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    parent = list(range(n))
    rank = [1] * n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> bool:
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        rank[px] += rank[py]
        return True

    for u, v in edges:
        if not union(u, v):
            return False  # cycle detected

    return True


# Test cases
if __name__ == "__main__":
    print(validTree(5, [[0,1],[0,2],[0,3],[1,4]]))  # True
    print(validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))  # False (cycle)
