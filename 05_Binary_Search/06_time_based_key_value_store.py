"""
Problem: Time Based Key-Value Store (LeetCode #981)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Are timestamps for the same key always increasing in set calls? (Yes)
- If no value exists at or before the given timestamp, return ""? (Yes)
- Can the same key be set multiple times? (Yes, with increasing timestamps)

APPROACH / PSEUDOCODE:
- Store: dict mapping key → list of (timestamp, value) pairs
- set(): append (timestamp, value) to key's list
- get(): binary search on the list for key to find largest timestamp <= given timestamp
    - Since timestamps are increasing, list is sorted → binary search works

Time Complexity: set O(1), get O(log n) where n = number of values for that key
Space Complexity: O(n) total stored entries
"""

import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        entries = self.store[key]
        # Find rightmost entry with timestamp <= given timestamp
        lo, hi = 0, len(entries) - 1
        result = ""

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if entries[mid][0] <= timestamp:
                result = entries[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1

        return result


# Test cases
if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))   # "bar"
    print(tm.get("foo", 3))   # "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))   # "bar2"
    print(tm.get("foo", 5))   # "bar2"
