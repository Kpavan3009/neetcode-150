"""
Problem: Binary Tree Right Side View (LeetCode #199)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Right side view = rightmost node visible at each level? (Yes)
- Empty tree returns []? (Yes)

APPROACH / PSEUDOCODE:
- BFS level by level; take the last node's value at each level
- That's what you'd see looking from the right

Time Complexity: O(n)
Space Complexity: O(n) - queue
"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# Test cases
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(rightSideView(root))  # [1, 3, 4]
    print(rightSideView(None))  # []
