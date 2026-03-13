"""
Problem: Maximum Depth of Binary Tree (LeetCode #104)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Depth = number of nodes along longest path from root to leaf? (Yes)
- Empty tree has depth 0? (Yes)

APPROACH / PSEUDOCODE:
- Recursive DFS: max_depth(node) = 1 + max(max_depth(left), max_depth(right))
- Base case: None node → return 0

Time Complexity: O(n) - visit every node
Space Complexity: O(h) - recursion depth (h = height)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# Iterative BFS approach
def maxDepth_bfs(root: Optional[TreeNode]) -> int:
    from collections import deque
    if not root:
        return 0
    depth = 0
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
    return depth


# Test cases
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(maxDepth(root))  # 3
    print(maxDepth(None))  # 0
