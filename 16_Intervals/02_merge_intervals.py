"""
Problem: Merge Intervals (LeetCode #56)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Intervals may not be sorted? (Yes, we sort them)
- Return merged non-overlapping intervals? (Yes)

APPROACH / PSEUDOCODE:
- Sort intervals by start time
- Iterate; if current interval overlaps with last merged (curr.start <= last.end):
    → merge by extending last's end to max(last.end, curr.end)
- Else: add current as new interval

Time Complexity: O(n log n) - sorting
Space Complexity: O(n) - output
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])

    return result


# Test cases
if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
    print(merge([[1,4],[4,5]]))                  # [[1,5]]
