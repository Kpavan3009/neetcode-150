"""
Problem: House Robber (LeetCode #198)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can't rob two adjacent houses? (Yes)
- Maximize total amount stolen? (Yes)
- Array can be empty or have 1 element? (Yes)

APPROACH / PSEUDOCODE:
- dp[i] = max money robbing from houses 0..i
- dp[i] = max(dp[i-1], dp[i-2] + nums[i])
  (either skip current house, or rob current + best from 2 houses ago)
- Optimize to O(1) space with two variables

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = curr

    return prev1


# Test cases
if __name__ == "__main__":
    print(rob([1,2,3,1]))      # 4 (rob 1 and 3)
    print(rob([2,7,9,3,1]))    # 12 (rob 2, 9, 1)
