"""
Problem: Burst Balloons (LeetCode #312)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Coins for bursting balloon i = nums[left] * nums[i] * nums[right]? (Yes, neighbors)
- Maximize total coins? (Yes)
- Boundary balloons (outside array) have value 1? (Yes)

APPROACH / PSEUDOCODE:
- Think in reverse: choose the LAST balloon to burst in each interval
- Pad array with 1s on both sides
- dp[left][right] = max coins for bursting all balloons between left and right (exclusive)
- For each balloon k as the last to burst in (left, right):
    dp[left][right] = max(dp[left][k] + nums[left]*nums[k]*nums[right] + dp[k][right])
- Fill table by interval length (bottom-up)

Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

from typing import List


def maxCoins(nums: List[int]) -> int:
    nums = [1] + nums + [1]  # pad with boundary 1s
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):  # interval length (at least 2 for exclusive bounds)
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):  # k is the last balloon in (left, right)
                coins = nums[left] * nums[k] * nums[right]
                dp[left][right] = max(dp[left][right],
                                      dp[left][k] + coins + dp[k][right])

    return dp[0][n - 1]


# Test cases
if __name__ == "__main__":
    print(maxCoins([3,1,5,8]))  # 167
    print(maxCoins([1,5]))      # 10
