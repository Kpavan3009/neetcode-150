"""
Problem: Alien Dictionary (LeetCode #269 / NeetCode)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Words are sorted lexicographically in alien language? (Yes)
- Return any valid character ordering? (Yes)
- Return "" if contradictions exist? (Yes)
- Return "" if cycle? (Yes)

APPROACH / PSEUDOCODE:
- Compare adjacent words to extract character order constraints (edges)
- If word1 is prefix of word2 but longer → invalid (e.g., "abc" before "ab")
- Build directed graph from constraints
- Topological sort (DFS) to find valid character order
- Cycle → return ""

Time Complexity: O(C) where C = total characters in all words
Space Complexity: O(1) - at most 26 characters
"""

from typing import List
from collections import defaultdict


def alienOrder(words: List[str]) -> str:
    # Initialize graph with all unique characters
    graph = {ch: set() for word in words for ch in word}

    # Extract ordering constraints from adjacent words
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""  # invalid: longer word is prefix
        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                break

    # Topological sort via DFS
    # state: 0=unvisited, 1=in-progress, 2=done
    state = {ch: 0 for ch in graph}
    result = []

    def dfs(ch: str) -> bool:
        if state[ch] == 1:
            return False  # cycle
        if state[ch] == 2:
            return True

        state[ch] = 1
        for neighbor in graph[ch]:
            if not dfs(neighbor):
                return False
        state[ch] = 2
        result.append(ch)
        return True

    for ch in graph:
        if not dfs(ch):
            return ""

    return ''.join(reversed(result))


# Test cases
if __name__ == "__main__":
    print(alienOrder(["wrt","wrf","er","ett","rftt"]))  # "wertf"
    print(alienOrder(["z","x"]))                         # "zx"
    print(alienOrder(["z","x","z"]))                     # "" (cycle)
