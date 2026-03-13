"""
Problem: Validate Binary Search Tree (LeetCode #98)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Strict BST: no duplicates? (Yes, left < node < right)
- Can values be negative or very large? (Yes, assume full int range)

APPROACH / PSEUDOCODE:
- DFS with valid range [min_val, max_val] at each node
- Root: range is (-inf, +inf)
- Going left: upper bound becomes current node's value
- Going right: lower bound becomes current node's value
- At each node: if not (min_val < node.val < max_val) → invalid

Time Complexity: O(n)
Space Complexity: O(h)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))


# Test cases
if __name__ == "__main__":
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(isValidBST(root1))  # True

    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(isValidBST(root2))  # False (4 < 5 but is in right subtree)
