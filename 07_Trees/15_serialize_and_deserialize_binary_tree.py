"""
Problem: Serialize and Deserialize Binary Tree (LeetCode #297)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Any serialization format acceptable? (Yes, as long as we can reconstruct)
- Handle any binary tree (not just BST)? (Yes)
- Can values be negative? (Yes)

APPROACH / PSEUDOCODE:
- Preorder DFS for both serialize and deserialize
- serialize: preorder traversal, use 'N' for null nodes, comma-separated
- deserialize: split by comma, use a pointer to reconstruct tree in preorder order
  - If 'N' → return None; otherwise create node, recurse left, recurse right

Time Complexity: O(n) for both
Space Complexity: O(n)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                result.append('N')
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(','))

        def dfs() -> Optional[TreeNode]:
            val = next(tokens)
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Test cases
if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    serialized = codec.serialize(root)
    print(serialized)  # "1,2,N,N,3,4,N,N,5,N,N"
    deserialized = codec.deserialize(serialized)
    print(deserialized.val)         # 1
    print(deserialized.right.val)   # 3
