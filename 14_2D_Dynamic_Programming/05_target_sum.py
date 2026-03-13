"""
Problem: Target Sum (LeetCode #494)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Assign + or - to each number? (Yes)
- Count ways to reach exactly the target? (Yes)
- Numbers can be 0? (Yes)

APPROACH / PSEUDOCODE:
- Let P = sum of positive subset, N = sum of negative subset
- P + N = total, P - N = target
- So P = (total + target) / 2
- Count subsets with sum P (0/1 knapsack, count version)
- If (total + target) is odd → return 0

Time Complexity: O(n * total)
Space Complexity: O(total)
"""

from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:
    total = sum(nums)

    # Edge case: target unreachable
    if abs(target) > total or (total + target) % 2 != 0:
        return 0

    pos_sum = (total + target) // 2
    dp = [0] * (pos_sum + 1)
    dp[0] = 1

    for num in nums:
        for j in range(pos_sum, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[pos_sum]


# Test cases
if __name__ == "__main__":
    print(findTargetSumWays([1,1,1,1,1], 3))  # 5
    print(findTargetSumWays([1], 1))            # 1
    print(findTargetSumWays([1], 2))            # 0
