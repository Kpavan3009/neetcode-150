"""
Problem: Network Delay Time (LeetCode #743)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Directed weighted graph? (Yes)
- Find time for signal to reach ALL nodes from k? (Yes)
- Return -1 if not all nodes reachable? (Yes)

APPROACH / PSEUDOCODE:
- Dijkstra's algorithm from source node k
- Use min-heap: (distance, node)
- Relax edges greedily; record shortest distance to each node
- Return max of all shortest distances (= time for slowest node to receive)
- Return -1 if some node not reached

Time Complexity: O((V + E) log V)
Space Complexity: O(V + E)
"""

import heapq
from collections import defaultdict
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]  # (distance, node)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1


# Test cases
if __name__ == "__main__":
    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
    print(networkDelayTime([[1,2,1]], 2, 1))                    # 1
    print(networkDelayTime([[1,2,1]], 2, 2))                    # -1
