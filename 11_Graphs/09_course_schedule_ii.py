"""
Problem: Course Schedule II (LeetCode #210)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Return valid ordering of courses? (Yes, topological sort)
- Return [] if impossible (cycle)? (Yes)
- Multiple valid orderings exist? (Yes, return any one)

APPROACH / PSEUDOCODE:
- Topological sort via DFS (post-order = reverse topological order)
- Same 3-state approach as Course Schedule I
- When DFS completes for a node → add to result
- Reverse result at the end for correct topological order

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = [0] * numCourses  # 0=unvisited, 1=in-progress, 2=done
    result = []

    def dfs(node: int) -> bool:
        if state[node] == 1:
            return False  # cycle
        if state[node] == 2:
            return True   # already processed

        state[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False

        state[node] = 2
        result.append(node)
        return True

    for i in range(numCourses):
        if not dfs(i):
            return []

    return result[::-1]  # reverse for correct topological order


# Test cases
if __name__ == "__main__":
    print(findOrder(2, [[1,0]]))                    # [0,1]
    print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))  # [0,2,1,3] or similar
    print(findOrder(1, []))                          # [0]
