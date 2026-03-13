"""
Problem: Koko Eating Bananas (LeetCode #875)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can she eat from multiple piles per hour? (No, at most one pile per hour)
- If she eats faster than pile size, does extra count toward next pile? (No)
- Is h guaranteed >= len(piles)? (Yes, so a valid speed always exists)
- What's the minimum speed? (1)

APPROACH / PSEUDOCODE:
- Binary search on the eating speed k (range: 1 to max(piles))
- For a given speed k, compute hours needed: sum(ceil(pile/k) for pile in piles)
- If hours <= h → speed k is feasible, try slower (right = mid)
- If hours > h → too slow, need faster speed (left = mid + 1)
- Return smallest feasible speed

Time Complexity: O(n log m) where n = len(piles), m = max(piles)
Space Complexity: O(1)
"""

from typing import List
import math


def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        hours = sum(math.ceil(pile / mid) for pile in piles)

        if hours <= h:
            right = mid        # feasible, try slower
        else:
            left = mid + 1     # too slow, need faster

    return left


# Test cases
if __name__ == "__main__":
    print(minEatingSpeed([3,6,7,11], 8))   # 4
    print(minEatingSpeed([30,11,23,4,20], 5))  # 30
    print(minEatingSpeed([30,11,23,4,20], 6))  # 23
