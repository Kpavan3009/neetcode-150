"""
Problem: Binary Tree Level Order Traversal (LeetCode #102)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Return list of lists, one per level? (Yes)
- Empty tree returns empty list? (Yes)
- Left to right order within each level? (Yes)

APPROACH / PSEUDOCODE:
- BFS using a queue
- At each step, process all nodes at current level (queue snapshot)
- For each node, add its value to level list and enqueue children
- Append level list to result after processing each level

Time Complexity: O(n)
Space Complexity: O(n) - queue holds up to n/2 nodes at last level
"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# Test cases
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(levelOrder(root))   # [[3],[9,20],[15,7]]
    print(levelOrder(None))   # []
