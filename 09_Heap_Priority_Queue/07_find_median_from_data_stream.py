"""
Problem: Find Median from Data Stream (LeetCode #295)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Numbers can be added in any order? (Yes)
- Need to handle both odd and even count? (Yes)
- Assume addNum and findMedian called in valid sequence? (Yes)

APPROACH / PSEUDOCODE:
- Maintain two heaps:
    - small: max-heap for lower half (negate for Python's min-heap)
    - large: min-heap for upper half
- Invariant: len(small) >= len(large), differ by at most 1
- addNum: push to small, then rebalance by moving max(small) to large if needed,
           then ensure small is at least as large as large
- findMedian: if odd → top of small; if even → average of both tops

Time Complexity: addNum O(log n), findMedian O(1)
Space Complexity: O(n)
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negated): lower half
        self.large = []  # min-heap: upper half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Ensure max(small) <= min(large)
        if self.large and (-self.small[0]) > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance sizes: small can be at most 1 larger than large
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


# Test cases
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 2.0
