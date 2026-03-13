"""
Problem: Last Stone Weight (LeetCode #1046)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Smash two heaviest: if equal both destroyed, if not equal smaller destroyed and larger reduced? (Yes)
- Return weight of last stone or 0 if none left? (Yes)

APPROACH / PSEUDOCODE:
- Use a max-heap (negate values in Python's min-heap)
- Each round: pop two heaviest, compute difference, push back if non-zero
- Continue until 0 or 1 stone remains

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    # Max-heap: negate values
    heap = [-s for s in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        if first != second:
            heapq.heappush(heap, -(first - second))

    return -heap[0] if heap else 0


# Test cases
if __name__ == "__main__":
    print(lastStoneWeight([2,7,4,1,8,1]))  # 1
    print(lastStoneWeight([1]))             # 1
