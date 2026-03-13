"""
Problem: Course Schedule (LeetCode #207)
Difficulty: Medium

CLARIFYING QUESTIONS:
- prerequisites[i] = [a, b] means b is prerequisite for a? (Yes)
- Detect if cycle exists in the directed graph? (Yes, cycle = impossible to finish)

APPROACH / PSEUDOCODE:
- Build adjacency list
- DFS cycle detection with 3 states: unvisited (0), in-progress (1), done (2)
- If we revisit an in-progress node → cycle found → return False
- If DFS completes without cycle → return True

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # 0 = unvisited, 1 = in progress, 2 = completed
    state = [0] * numCourses

    def dfs(node: int) -> bool:
        if state[node] == 1:
            return False  # cycle detected
        if state[node] == 2:
            return True   # already verified

        state[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        state[node] = 2
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True


# Test cases
if __name__ == "__main__":
    print(canFinish(2, [[1,0]]))         # True (0→1, no cycle)
    print(canFinish(2, [[1,0],[0,1]]))   # False (cycle: 0→1→0)
