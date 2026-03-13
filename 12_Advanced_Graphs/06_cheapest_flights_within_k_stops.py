"""
Problem: Cheapest Flights Within K Stops (LeetCode #787)
Difficulty: Medium

CLARIFYING QUESTIONS:
- At most k stops (not k+1 edges)? (Yes, k stops = k+1 edges)
- Return -1 if no route exists? (Yes)
- Can there be multiple edges between same nodes? (Yes)

APPROACH / PSEUDOCODE:
- Bellman-Ford variant: relax edges exactly k+1 times (at most k stops)
- Use two arrays: prev_prices (from previous round) and curr_prices
- This ensures we don't use more than k+1 edges in one iteration

Time Complexity: O(k * E) where E = number of flights
Space Complexity: O(n) for price arrays
"""

from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    INF = float('inf')
    prices = [INF] * n
    prices[src] = 0

    for _ in range(k + 1):  # at most k+1 edges (k stops)
        temp = prices[:]
        for u, v, w in flights:
            if prices[u] != INF and prices[u] + w < temp[v]:
                temp[v] = prices[u] + w
        prices = temp

    return prices[dst] if prices[dst] != INF else -1


# Test cases
if __name__ == "__main__":
    print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # 700
    print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # 200
    print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # 500
