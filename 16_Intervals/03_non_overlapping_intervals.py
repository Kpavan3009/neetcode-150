"""
Problem: Non-overlapping Intervals (LeetCode #435)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Minimum removals to make remaining intervals non-overlapping? (Yes)
- Intervals touching at a point (e.g., [1,2] and [2,3]) are non-overlapping? (Yes)

APPROACH / PSEUDOCODE:
- Sort by end time (greedy: keep interval that ends earliest → leaves room for more)
- For each interval:
    - If it starts >= previous end → no overlap, keep it, update prev end
    - Else → overlap, remove current (increment removals), keep previous (ends sooner)

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])  # sort by end time
    removals = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prev_end:
            prev_end = end  # no overlap, extend
        else:
            removals += 1  # overlap, remove current (keep the one ending sooner = prev)

    return removals


# Test cases
if __name__ == "__main__":
    print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # 1 (remove [1,3])
    print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))        # 2
    print(eraseOverlapIntervals([[1,2],[2,3]]))              # 0
