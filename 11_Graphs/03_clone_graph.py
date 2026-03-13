"""
Problem: Clone Graph (LeetCode #133)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Deep copy (new nodes for everything)? (Yes)
- Can graph have cycles? (Yes)
- Can graph be empty (None)? (Yes, return None)

APPROACH / PSEUDOCODE:
- Use DFS with a hash map: original_node → cloned_node
- If node already cloned → return its clone (handles cycles)
- Otherwise: create clone, store in map, recursively clone all neighbors

Time Complexity: O(V + E)
Space Complexity: O(V) - hash map + recursion stack
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None

    cloned = {}  # original -> clone

    def dfs(n: Node) -> Node:
        if n in cloned:
            return cloned[n]

        clone = Node(n.val)
        cloned[n] = clone

        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


# Test cases
if __name__ == "__main__":
    # Build graph: 1 -- 2 -- 3 -- 4 -- 1 (cycle)
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n3, n1]

    cloned_root = cloneGraph(n1)
    print(cloned_root.val)  # 1
    print([n.val for n in cloned_root.neighbors])  # [2, 4]
    print(cloned_root is n1)  # False (deep copy)
