"""
Problem: Kth Smallest Element in a BST (LeetCode #230)
Difficulty: Medium

CLARIFYING QUESTIONS:
- k is always valid (1 <= k <= number of nodes)? (Yes)
- Inorder traversal of BST gives sorted order? (Yes, that's the key insight)

APPROACH / PSEUDOCODE:
- Iterative inorder traversal (left → root → right) using a stack
- Count nodes visited; when count == k → return current node's value
- No need to traverse entire tree

Time Complexity: O(H + k) where H = height
Space Complexity: O(H) - stack
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val

        curr = curr.right

    return -1  # should never reach here given valid input


# Test cases
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(kthSmallest(root, 1))  # 1

    root2 = TreeNode(5,
        TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
        TreeNode(6))
    print(kthSmallest(root2, 3))  # 3
