"""
Problem: Invert Binary Tree (LeetCode #226)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Invert in place or return new tree? (In place, return root)
- Can tree be empty? (Yes, return None)

APPROACH / PSEUDOCODE:
- Recursively swap left and right children for every node
- Base case: if node is None, return None
- Swap children, then recursively invert each subtree

Time Complexity: O(n) - visit every node
Space Complexity: O(h) - recursion stack, h = height (O(log n) balanced, O(n) worst)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)

    return root


# Test cases
if __name__ == "__main__":
    # [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
    root = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9))
    )
    inverted = invertTree(root)
    print(inverted.val)         # 4
    print(inverted.left.val)    # 7
    print(inverted.right.val)   # 2
