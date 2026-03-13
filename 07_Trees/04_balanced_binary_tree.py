"""
Problem: Balanced Binary Tree (LeetCode #110)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Height-balanced: every node's left and right subtree heights differ by at most 1? (Yes)
- Empty tree is balanced? (Yes)

APPROACH / PSEUDOCODE:
- DFS: compute height of each subtree and check balance simultaneously
- If a subtree is unbalanced, return -1 as sentinel
- At each node: if left == -1 or right == -1 or abs(left-right) > 1 → return -1
- Otherwise return actual height

Time Complexity: O(n)
Space Complexity: O(h)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = dfs(node.left)
        if left == -1:
            return -1
        right = dfs(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return dfs(root) != -1


# Test cases
if __name__ == "__main__":
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(isBalanced(root1))  # True

    root2 = TreeNode(1,
        TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
        TreeNode(2))
    print(isBalanced(root2))  # False
