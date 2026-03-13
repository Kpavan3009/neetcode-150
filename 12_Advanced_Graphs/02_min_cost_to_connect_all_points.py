"""
Problem: Min Cost to Connect All Points (LeetCode #1584)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Cost between two points = Manhattan distance? (Yes: |x1-x2| + |y1-y2|)
- Connect all n points with minimum total cost? (Yes, this is a Minimum Spanning Tree problem)
- Can points overlap? (No)

APPROACH / PSEUDOCODE:
- Prim's Algorithm for MST:
    - Start with any node; use a min-heap
    - Greedily pick cheapest edge to an unvisited node
    - Add that node's edges to heap
    - Repeat until all nodes visited

Time Complexity: O(n^2 log n)
Space Complexity: O(n^2) - heap can hold all edges
"""

import heapq
from typing import List


def minCostConnectPoints(points: List[List[int]]) -> int:
    n = len(points)
    visited = set()
    heap = [(0, 0)]  # (cost, node_index)
    total_cost = 0

    while len(visited) < n:
        cost, i = heapq.heappop(heap)
        if i in visited:
            continue

        visited.add(i)
        total_cost += cost

        for j in range(n):
            if j not in visited:
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (dist, j))

    return total_cost


# Test cases
if __name__ == "__main__":
    print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))  # 20
    print(minCostConnectPoints([[3,12],[-2,5],[-4,1]]))             # 18
