"""
Problem: Jump Game (LeetCode #55)
Difficulty: Medium

CLARIFYING QUESTIONS:
- nums[i] = max jump length from position i? (Yes)
- Can we reach the last index? (Determine yes/no)
- Minimum 1 element? (Yes)

APPROACH / PSEUDOCODE:
- Track the farthest reachable index
- At each position i: if i > max_reach → can't reach → return False
- Update max_reach = max(max_reach, i + nums[i])
- If max_reach >= last index → True

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def canJump(nums: List[int]) -> bool:
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True


# Test cases
if __name__ == "__main__":
    print(canJump([2,3,1,1,4]))  # True
    print(canJump([3,2,1,0,4]))  # False
