"""
Problem: Kth Largest Element in a Stream (LeetCode #703)
Difficulty: Easy

CLARIFYING QUESTIONS:
- The stream always has at least k elements when add() is called? (Yes)
- k is consistent throughout? (Yes)
- What if initial nums has fewer than k elements? (Still valid, add() will bring it up)

APPROACH / PSEUDOCODE:
- Use a min-heap of size k
- The root of the heap = kth largest element
- On add(val): push val to heap; if size > k → pop (removes smallest, maintains top-k)
- Return heap root (= kth largest)

Time Complexity: O(log k) per add()
Space Complexity: O(k)
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Test cases
if __name__ == "__main__":
    kl = KthLargest(3, [4, 5, 8, 2])
    print(kl.add(3))   # 4
    print(kl.add(5))   # 5
    print(kl.add(10))  # 8
    print(kl.add(9))   # 8
    print(kl.add(4))   # 8
