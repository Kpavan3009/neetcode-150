"""
Problem: Min Cost Climbing Stairs (LeetCode #746)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Can start from step 0 or step 1? (Yes)
- After paying cost[i], can go 1 or 2 steps? (Yes)
- Reach the top (index beyond last element)? (Yes)

APPROACH / PSEUDOCODE:
- dp[i] = min cost to reach step i
- dp[0] = cost[0], dp[1] = cost[1]
- dp[i] = cost[i] + min(dp[i-1], dp[i-2])
- Answer = min(dp[n-1], dp[n-2])

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    prev2, prev1 = cost[0], cost[1]

    for i in range(2, n):
        curr = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = curr

    return min(prev1, prev2)


# Test cases
if __name__ == "__main__":
    print(minCostClimbingStairs([10,15,20]))     # 15
    print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))  # 6
