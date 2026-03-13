"""
Problem: Partition Equal Subset Sum (LeetCode #416)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Partition into exactly 2 subsets? (Yes)
- Can the array have negative numbers? (No, all positive)
- Both subsets must be non-empty? (Yes)

APPROACH / PSEUDOCODE:
- Target = total sum / 2 (if odd sum → impossible)
- Reduce to: can we pick a subset with sum = target? (0/1 Knapsack)
- dp[j] = True if subset sum j is achievable
- For each num, update dp backwards: dp[j] |= dp[j - num]
  (backwards to avoid using same element twice)

Time Complexity: O(n * target)
Space Complexity: O(target)
"""

from typing import List


def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = {0}  # set of achievable sums

    for num in nums:
        dp = dp | {s + num for s in dp}
        if target in dp:
            return True

    return target in dp


# Boolean array approach (more cache-friendly):
def canPartition_v2(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


# Test cases
if __name__ == "__main__":
    print(canPartition([1,5,11,5]))   # True ([1,5,5] and [11])
    print(canPartition([1,2,3,5]))    # False
