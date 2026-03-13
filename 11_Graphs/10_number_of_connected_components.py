"""
Problem: Number of Connected Components in an Undirected Graph (LeetCode #323 / NeetCode)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Undirected graph? (Yes)
- n nodes numbered 0 to n-1? (Yes)
- Edges are bidirectional? (Yes)

APPROACH / PSEUDOCODE:
- Union-Find (Disjoint Set Union) approach
- Initialize each node as its own component
- For each edge, union the two endpoints
- Count distinct roots = number of components

Time Complexity: O(n + E * alpha(n)) ≈ O(n + E) with path compression
Space Complexity: O(n)
"""

from typing import List


def countComponents(n: int, edges: List[List[int]]) -> int:
    parent = list(range(n))
    rank = [1] * n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path compression
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

    components = n
    for u, v in edges:
        if union(u, v):
            components -= 1

    return components


# Test cases
if __name__ == "__main__":
    print(countComponents(5, [[0,1],[1,2],[3,4]]))         # 2
    print(countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))   # 1
