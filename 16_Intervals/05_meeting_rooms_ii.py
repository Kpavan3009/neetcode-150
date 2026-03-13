"""
Problem: Meeting Rooms II (LeetCode #253 / NeetCode)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Minimum number of conference rooms needed? (Yes)
- Same person can attend back-to-back meetings? (Yes, end == next start is fine)

APPROACH / PSEUDOCODE:
- Use a min-heap of end times of ongoing meetings
- Sort meetings by start time
- For each meeting:
    - If heap non-empty and top (earliest end) <= current start → reuse that room (pop)
    - Push current end time to heap
- Heap size = number of rooms needed

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import heapq
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = []  # min-heap of end times

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)  # reuse the earliest-ending room
        else:
            heapq.heappush(heap, end)     # need a new room

    return len(heap)


# Test cases
if __name__ == "__main__":
    print(minMeetingRooms([[0,30],[5,10],[15,20]]))  # 2
    print(minMeetingRooms([[7,10],[2,4]]))            # 1
