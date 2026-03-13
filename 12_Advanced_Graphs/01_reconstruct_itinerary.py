"""
Problem: Reconstruct Itinerary (LeetCode #332)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Start from JFK always? (Yes)
- Must use all tickets exactly once? (Yes)
- If multiple valid itineraries, return lexically smallest? (Yes)
- Input guarantees a valid itinerary exists? (Yes)

APPROACH / PSEUDOCODE:
- Build adjacency list with sorted destinations (for lexical order)
- Hierholzer's algorithm for Eulerian path:
    - DFS: greedily pick smallest destination
    - When stuck (no more neighbors), add to result
    - Reverse result at end
- Sort adjacency lists so we always pick lexically smallest first

Time Complexity: O(E log E) - sorting adjacency lists
Space Complexity: O(E)
"""

from typing import List
from collections import defaultdict


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    result = []

    def dfs(airport: str) -> None:
        while graph[airport]:
            dfs(graph[airport].pop())
        result.append(airport)

    dfs("JFK")
    return result[::-1]


# Test cases
if __name__ == "__main__":
    print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    # ["JFK","MUC","LHR","SFO","SJC"]

    print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    # ["JFK","ATL","JFK","SFO","ATL","SFO"]
