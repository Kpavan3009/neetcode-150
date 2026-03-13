"""
Problem: Coin Change II (LeetCode #518)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Count number of combinations (not permutations)? (Yes, order doesn't matter)
- Unlimited coins of each denomination? (Yes)
- Return 0 if impossible? (Yes)

APPROACH / PSEUDOCODE:
- Unbounded knapsack problem
- dp[j] = number of ways to make amount j
- dp[0] = 1 (base case: one way to make 0)
- For each coin, iterate amounts from coin to target:
    dp[j] += dp[j - coin]
- Process coins in outer loop to avoid counting permutations

Time Complexity: O(n * amount) where n = number of coins
Space Complexity: O(amount)
"""

from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1  # one way to make 0: use no coins

    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]

    return dp[amount]


# Test cases
if __name__ == "__main__":
    print(change(5, [1,2,5]))   # 4 ([1,1,1,1,1],[1,1,1,2],[1,2,2],[5])
    print(change(3, [2]))       # 0
    print(change(10, [10]))     # 1
