"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal (LeetCode #105)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Are all values unique? (Yes)
- Both arrays have the same elements? (Yes)
- Return the root of constructed tree? (Yes)

APPROACH / PSEUDOCODE:
- Preorder: first element is always the root
- Inorder: elements left of root = left subtree; right of root = right subtree
- Use a hash map for O(1) index lookup in inorder array
- Recursively: root = preorder[pre_idx], find in inorder, recurse on halves

Time Complexity: O(n)
Space Complexity: O(n) - hash map + recursion stack
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inorder_index = {val: i for i, val in enumerate(inorder)}
    pre_idx = [0]  # mutable pointer

    def build(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        root_val = preorder[pre_idx[0]]
        pre_idx[0] += 1
        root = TreeNode(root_val)

        mid = inorder_index[root_val]
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)

        return root

    return build(0, len(inorder) - 1)


# Test cases
if __name__ == "__main__":
    root = buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(root.val)         # 3
    print(root.left.val)    # 9
    print(root.right.val)   # 20
