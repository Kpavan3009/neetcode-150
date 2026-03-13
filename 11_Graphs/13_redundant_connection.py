"""
Problem: Redundant Connection (LeetCode #684)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Undirected graph; find edge that creates a cycle? (Yes)
- Return the edge that appears last in the input if multiple? (Yes)
- n nodes, n edges initially forms a tree + 1 extra edge? (Yes)

APPROACH / PSEUDOCODE:
- Union-Find: process edges one by one
- If both endpoints already in same component → this edge creates cycle → return it
- Otherwise → union them
- The first cycle-creating edge (in order) is the answer

Time Complexity: O(n * alpha(n)) ≈ O(n)
Space Complexity: O(n)
"""

from typing import List


def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    parent = list(range(n + 1))
    rank = [1] * (n + 1)

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
            return [u, v]

    return []


# Test cases
if __name__ == "__main__":
    print(findRedundantConnection([[1,2],[1,3],[2,3]]))         # [2,3]
    print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # [1,4]
