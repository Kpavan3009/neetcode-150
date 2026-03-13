"""
Problem: Insert Interval (LeetCode #57)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Existing intervals sorted and non-overlapping? (Yes)
- Can newInterval overlap with multiple existing ones? (Yes, merge all)
- Can newInterval be before/after all existing intervals? (Yes)

APPROACH / PSEUDOCODE:
- Add all intervals that come before newInterval (end < newInterval.start)
- Merge all overlapping intervals with newInterval (start <= merged.end)
    - Expand merged interval: min(start), max(end)
- Add remaining intervals that come after merged interval
- Add the merged interval

Time Complexity: O(n)
Space Complexity: O(n) - output array
"""

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# Test cases
if __name__ == "__main__":
    print(insert([[1,3],[6,9]], [2,5]))          # [[1,5],[6,9]]
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]
