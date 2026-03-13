"""
Problem: Kth Largest Element in an Array (LeetCode #215)
Difficulty: Medium

CLARIFYING QUESTIONS:
- kth largest in sorted order (not distinct)? (Yes)
- Is k always valid? (Yes)
- Can I use sorting? (Yes, but O(n log n); optimal is O(n) via quickselect)

APPROACH 1 - Min-Heap:
- Maintain min-heap of size k; root = kth largest
- Time: O(n log k), Space: O(k)

APPROACH 2 - Quickselect (optimal):
- Partition array like quicksort; recursively narrow to kth position
- Time: O(n) average, O(n^2) worst, Space: O(1)
"""

import heapq
import random
from typing import List


# Approach 1: Min-Heap
def findKthLargest_heap(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


# Approach 2: Quickselect (average O(n))
def findKthLargest(nums: List[int], k: int) -> int:
    target = len(nums) - k  # kth largest = target-th smallest (0-indexed)

    def quickselect(left: int, right: int) -> int:
        pivot = nums[right]
        p = left  # partition pointer

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        nums[p], nums[right] = nums[right], nums[p]

        if p == target:
            return nums[p]
        elif p < target:
            return quickselect(p + 1, right)
        else:
            return quickselect(left, p - 1)

    return quickselect(0, len(nums) - 1)


# Test cases
if __name__ == "__main__":
    print(findKthLargest([3,2,1,5,6,4], 2))     # 5
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # 4
