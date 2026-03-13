"""
Problem: Minimum Interval to Include Each Query (LeetCode #1851)
Difficulty: Hard

CLARIFYING QUESTIONS:
- For each query, find smallest interval containing it? (Yes, size = right-left+1)
- Return -1 if no interval contains the query? (Yes)
- Queries independent of each other? (Yes)

APPROACH / PSEUDOCODE:
- Sort intervals by start, sort queries (keeping original indices)
- Min-heap by interval size (size, end) for active intervals
- For each query (sorted):
    - Add all intervals with start <= query to heap
    - Remove intervals from heap that end < query (expired)
    - Heap top = smallest valid interval for this query

Time Complexity: O((n + q) log n)
Space Complexity: O(n + q)
"""

import heapq
from typing import List


def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals.sort()
    queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])
    result = [-1] * len(queries)

    heap = []  # (size, end)
    i = 0

    for idx, q in queries_sorted:
        # Add all intervals starting at or before q
        while i < len(intervals) and intervals[i][0] <= q:
            start, end = intervals[i]
            heapq.heappush(heap, (end - start + 1, end))
            i += 1

        # Remove expired intervals (end < q)
        while heap and heap[0][1] < q:
            heapq.heappop(heap)

        if heap:
            result[idx] = heap[0][0]

    return result


# Test cases
if __name__ == "__main__":
    print(minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))  # [3,3,1,4]
    print(minInterval([[2,3],[2,5],[1,8],[20,25]], [2,19,22]))  # [2,-1,6]
