"""
Problem: House Robber II (LeetCode #213)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Houses arranged in a circle (first and last are adjacent)? (Yes)
- Can't rob adjacent houses? (Yes)
- Single house case? (Return that house's value)

APPROACH / PSEUDOCODE:
- Break circular constraint: solve two sub-problems
    1. Rob houses 0 to n-2 (exclude last)
    2. Rob houses 1 to n-1 (exclude first)
- Answer = max of both sub-problems
- Reuse linear House Robber solution

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    def rob_linear(houses: List[int]) -> int:
        prev2, prev1 = houses[0], max(houses[0], houses[1])
        for i in range(2, len(houses)):
            curr = max(prev1, prev2 + houses[i])
            prev2 = prev1
            prev1 = curr
        return prev1

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Test cases
if __name__ == "__main__":
    print(rob([2,3,2]))     # 3
    print(rob([1,2,3,1]))   # 4
    print(rob([1,2,3]))     # 3
