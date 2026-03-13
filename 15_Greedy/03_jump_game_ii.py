"""
Problem: Jump Game II (LeetCode #45)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Always possible to reach last index? (Yes)
- Minimize number of jumps? (Yes)
- nums[i] = max jump length? (Yes)

APPROACH / PSEUDOCODE:
- Greedy BFS-like: process windows of indices reachable in each jump
- current_end = farthest index reachable with current number of jumps
- farthest = farthest index reachable from any position in current window
- When we reach current_end → increment jumps, set current_end = farthest

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def jump(nums: List[int]) -> int:
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):  # don't need to jump from last position
        farthest = max(farthest, i + nums[i])
        if i == current_end:  # reached end of current jump range
            jumps += 1
            current_end = farthest

    return jumps


# Test cases
if __name__ == "__main__":
    print(jump([2,3,1,1,4]))  # 2 (jump to 3, jump to end)
    print(jump([2,3,0,1,4]))  # 2
