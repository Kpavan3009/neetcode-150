"""
Problem: Same Tree (LeetCode #100)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Same structure AND same values? (Yes)
- Two empty trees are the same? (Yes)

APPROACH / PSEUDOCODE:
- Recursive: if both None → True; if one None → False; if values differ → False
- Recursively check left and right subtrees

Time Complexity: O(n)
Space Complexity: O(h)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Test cases
if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(isSameTree(t1, t2))  # True

    t3 = TreeNode(1, TreeNode(2))
    t4 = TreeNode(1, None, TreeNode(2))
    print(isSameTree(t3, t4))  # False
