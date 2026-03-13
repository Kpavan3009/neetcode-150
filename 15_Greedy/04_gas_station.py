"""
Problem: Gas Station (LeetCode #134)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Circular route - can start from any station? (Yes)
- Return starting station index (or -1 if impossible)? (Yes)
- Unique answer guaranteed if it exists? (Yes)

APPROACH / PSEUDOCODE:
- If total gas >= total cost → a solution exists
- Greedy: track current tank balance
- If tank goes negative, the starting point from that segment failed
    → reset tank to 0, set next station as new candidate start
- Why this works: if sum(gas) >= sum(cost), the segment with positive prefix
  can carry us through the segment with negative prefix

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    tank = 0
    start = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1

    return start


# Test cases
if __name__ == "__main__":
    print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # 3
    print(canCompleteCircuit([2,3,4], [3,4,3]))           # -1
