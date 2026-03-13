"""
Problem: Task Scheduler (LeetCode #621)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Tasks with same label must be separated by at least n intervals? (Yes)
- CPU can be idle to fulfill cooling requirement? (Yes)
- Minimize total intervals (including idle)? (Yes)

APPROACH / PSEUDOCODE:
- Use a max-heap for task frequencies + a queue for cooling period
- Greedy: always execute the most frequent task available
- Each "round": pop max-freq task, decrement, add to cooldown queue with time available
- If heap empty but cooldown queue non-empty → idle
- When cooldown expires, push back to heap

Time Complexity: O(n * k) where n = number of tasks, k = unique task types
Space Complexity: O(1) - at most 26 unique tasks
"""

import heapq
from collections import Counter, deque


def leastInterval(tasks: list, n: int) -> int:
    count = Counter(tasks)
    heap = [-c for c in count.values()]
    heapq.heapify(heap)

    cooldown = deque()  # stores (-remaining_count, available_at_time)
    time = 0

    while heap or cooldown:
        time += 1

        if heap:
            cnt = heapq.heappop(heap) + 1  # execute task, decrement count
            if cnt < 0:  # still has remaining executions
                cooldown.append((cnt, time + n))

        if cooldown and cooldown[0][1] == time:
            heapq.heappush(heap, cooldown.popleft()[0])

    return time


# Test cases
if __name__ == "__main__":
    print(leastInterval(["A","A","A","B","B","B"], 2))  # 8
    print(leastInterval(["A","C","A","B","D","B"], 1))  # 6
    print(leastInterval(["A","A","A","B","B","B"], 3))  # 10
