"""
Problem: Binary Tree Maximum Path Sum (LeetCode #124)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Path can start and end at any node? (Yes)
- Path must be contiguous (connected)? (Yes, no skipping)
- Can all values be negative? (Yes, then answer is the max single node)

APPROACH / PSEUDOCODE:
- DFS: at each node compute max gain (max contribution to its parent's path)
- gain = max(0, left_gain) + max(0, right_gain) + node.val (path through this node)
- Update global max with this value
- Return node.val + max(left_gain, right_gain, 0) to parent (can only extend one side)

Time Complexity: O(n)
Space Complexity: O(h)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    max_sum = [float('-inf')]

    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        # Path sum through this node
        path_sum = node.val + left_gain + right_gain
        max_sum[0] = max(max_sum[0], path_sum)

        # Can only extend one direction to parent
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return max_sum[0]


# Test cases
if __name__ == "__main__":
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(maxPathSum(root1))  # 6

    root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(maxPathSum(root2))  # 42 (15 + 20 + 7)
