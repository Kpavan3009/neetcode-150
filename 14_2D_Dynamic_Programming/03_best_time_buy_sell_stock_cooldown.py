"""
Problem: Best Time to Buy and Sell Stock with Cooldown (LeetCode #309)
Difficulty: Medium

CLARIFYING QUESTIONS:
- After selling, must wait one day (cooldown) before buying again? (Yes)
- Can hold at most one stock at a time? (Yes)
- Maximize profit? (Yes)

APPROACH / PSEUDOCODE:
- States at each day:
    - holding: max profit when holding a stock
    - sold: max profit on day of selling (must cooldown next day)
    - cooldown: max profit on cooldown day (free to buy next day)
- Transitions:
    - holding = max(prev_holding, prev_cooldown - price)
    - sold = prev_holding + price
    - cooldown = max(prev_cooldown, prev_sold)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    holding = float('-inf')  # profit when holding a stock
    sold = 0                 # profit on day of selling
    cooldown = 0             # profit on cooldown/idle day

    for price in prices:
        prev_holding = holding
        prev_sold = sold
        prev_cooldown = cooldown

        holding = max(prev_holding, prev_cooldown - price)
        sold = prev_holding + price
        cooldown = max(prev_cooldown, prev_sold)

    return max(sold, cooldown)


# Test cases
if __name__ == "__main__":
    print(maxProfit([1,2,3,0,2]))  # 3 (buy@1, sell@3, cooldown, buy@0, sell@2)
    print(maxProfit([1]))          # 0
