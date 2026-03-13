"""
Problem: Best Time to Buy and Sell Stock (LeetCode #121)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Can I only make one transaction (buy once, sell once)? (Yes)
- Must I buy before I sell? (Yes)
- What if prices are always decreasing? (Return 0, no profit possible)
- Can prices be negative? (No, prices are positive)

APPROACH / PSEUDOCODE:
- Track the minimum price seen so far (best buy day)
- For each day, compute profit = current price - min price so far
- Update max profit if current profit is better
- Update min price if current price is lower

Time Complexity: O(n) - single pass
Space Complexity: O(1)
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


# Test cases
if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # 5 (buy at 1, sell at 6)
    print(maxProfit([7, 6, 4, 3, 1]))     # 0 (no profit possible)
