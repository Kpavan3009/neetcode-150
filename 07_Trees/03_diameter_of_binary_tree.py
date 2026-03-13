"""
Problem: Diameter of Binary Tree (LeetCode #543)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Diameter = longest path between any two nodes (may not pass through root)? (Yes)
- Length = number of edges? (Yes)
- Tree can be a single node (diameter = 0)? (Yes)

APPROACH / PSEUDOCODE:
- DFS: at each node compute height of left and right subtrees
- Diameter through current node = left_height + right_height
- Update global maximum diameter
- Return height of current node = 1 + max(left_height, right_height)

Time Complexity: O(n)
Space Complexity: O(h) - recursion depth
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    max_diameter = [0]

    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        max_diameter[0] = max(max_diameter[0], left + right)
        return 1 + max(left, right)

    dfs(root)
    return max_diameter[0]


# Test cases
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(diameterOfBinaryTree(root))  # 3 (path: 4→2→1→3 or 5→2→1→3)
    print(diameterOfBinaryTree(TreeNode(1, TreeNode(2))))  # 1
