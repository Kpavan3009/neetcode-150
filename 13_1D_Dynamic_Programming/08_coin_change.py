"""
Problem: Coin Change (LeetCode #322)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Unlimited coins of each denomination? (Yes)
- Minimize number of coins? (Yes)
- Return -1 if impossible? (Yes)

APPROACH / PSEUDOCODE:
- dp[amount] = min coins needed to make that amount
- dp[0] = 0; all others = infinity
- For each amount from 1 to target:
    For each coin: if coin <= amount → dp[amount] = min(dp[amount], 1 + dp[amount - coin])
- Return dp[amount] if not infinity, else -1

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != float('inf') else -1


# Test cases
if __name__ == "__main__":
    print(coinChange([1,2,5], 11))  # 3 (5+5+1)
    print(coinChange([2], 3))       # -1
    print(coinChange([1], 0))       # 0
