"""
Problem: Subtree of Another Tree (LeetCode #572)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Is subRoot a subtree if it matches any subtree of root? (Yes, rooted at any node)
- Two empty trees → True? (Yes)
- subRoot can be larger than root? (Yes, but then return False)

APPROACH / PSEUDOCODE:
- For each node in root, check if the subtree rooted there equals subRoot
- Use isSameTree helper from previous problem
- DFS: check current node, then recurse left and right

Time Complexity: O(m * n) where m = nodes in root, n = nodes in subRoot
Space Complexity: O(h) recursion depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
        return True
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Test cases
if __name__ == "__main__":
    root = TreeNode(3,
        TreeNode(4, TreeNode(1), TreeNode(2)),
        TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    print(isSubtree(root, subRoot))  # True

    root2 = TreeNode(3,
        TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))),
        TreeNode(5))
    print(isSubtree(root2, subRoot))  # False
