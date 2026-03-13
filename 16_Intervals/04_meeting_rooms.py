"""
Problem: Meeting Rooms (LeetCode #252 / NeetCode)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Can a person attend all meetings? (Yes/no - detect overlap)
- Meetings are [start, end] pairs? (Yes)
- Meetings that touch (end == next start) are OK? (Yes)

APPROACH / PSEUDOCODE:
- Sort meetings by start time
- Check consecutive meetings for overlap: prev.end > next.start → conflict

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:  # overlap
            return False

    return True


# Test cases
if __name__ == "__main__":
    print(canAttendMeetings([[0,30],[5,10],[15,20]]))  # False
    print(canAttendMeetings([[7,10],[2,4]]))            # True
