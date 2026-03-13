"""
Problem: K Closest Points to Origin (LeetCode #973)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Distance = Euclidean distance? (Yes, but we can compare squared distances to avoid sqrt)
- Output order doesn't matter? (No, any order is fine)
- What if multiple points have same distance? (Any k are acceptable)

APPROACH / PSEUDOCODE:
- Use a max-heap of size k to maintain k closest points
- For each point: compute squared distance, push (-dist, point) to heap
- If heap size > k → pop the farthest (heap root = max distance)
- Return all points in heap

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []  # max-heap using negative distances

    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(heap, (-dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)

    return [[x, y] for _, x, y in heap]


# Alternative: sort by distance O(n log n)
# return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]


# Test cases
if __name__ == "__main__":
    print(kClosest([[1,3],[-2,2]], 1))          # [[-2,2]]
    print(kClosest([[3,3],[5,-1],[-2,4]], 2))   # [[3,3],[-2,4]]
