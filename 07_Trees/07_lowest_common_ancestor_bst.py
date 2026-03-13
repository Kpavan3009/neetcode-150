"""
Problem: Lowest Common Ancestor of a Binary Search Tree (LeetCode #235)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Both p and q are guaranteed to exist in the tree? (Yes)
- Can p == q? (Yes, LCA is p itself)
- Exploit BST property? (Yes, that's the key insight)

APPROACH / PSEUDOCODE:
- BST property: left < root < right
- If both p and q are less than current node → LCA is in left subtree
- If both p and q are greater than current node → LCA is in right subtree
- Otherwise current node is the LCA (split point)

Time Complexity: O(h) - h = height of tree
Space Complexity: O(1) iterative
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root

    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr  # Split point = LCA

    return curr


# Test cases
if __name__ == "__main__":
    root = TreeNode(6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9)))

    p, q = TreeNode(2), TreeNode(8)
    print(lowestCommonAncestor(root, p, q).val)  # 6

    p2, q2 = TreeNode(2), TreeNode(4)
    print(lowestCommonAncestor(root, p2, q2).val)  # 2
