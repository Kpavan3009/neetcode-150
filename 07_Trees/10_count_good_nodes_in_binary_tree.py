"""
Problem: Count Good Nodes in Binary Tree (LeetCode #1448)
Difficulty: Medium

CLARIFYING QUESTIONS:
- A good node is one where no node on root-to-that-node path has a greater value? (Yes)
- Root is always good? (Yes)

APPROACH / PSEUDOCODE:
- DFS, passing max value seen so far on current path
- At each node: if node.val >= max_so_far → it's a good node, count it
- Recurse with updated max

Time Complexity: O(n)
Space Complexity: O(h)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
    def dfs(node: Optional[TreeNode], max_val: int) -> int:
        if not node:
            return 0
        count = 1 if node.val >= max_val else 0
        new_max = max(max_val, node.val)
        count += dfs(node.left, new_max)
        count += dfs(node.right, new_max)
        return count

    return dfs(root, float('-inf'))


# Test cases
if __name__ == "__main__":
    root = TreeNode(3,
        TreeNode(1, TreeNode(3)),
        TreeNode(4, TreeNode(1), TreeNode(5)))
    print(goodNodes(root))  # 4
