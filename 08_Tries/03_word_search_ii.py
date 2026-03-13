"""
Problem: Word Search II (LeetCode #212)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Same word can be used multiple times in the board? (No, each cell used once per word)
- Return all words found (no duplicates)? (Yes)
- Can the words list have duplicates? (Assume no)

APPROACH / PSEUDOCODE:
- Build a Trie from all words
- DFS from each cell in the board
- At each step, traverse Trie alongside board path
- If current Trie node marks end_of_word → add word to results
- Mark cell as visited during DFS (use '#'), restore after backtrack
- Prune Trie nodes after finding a word to avoid revisiting

Time Complexity: O(M * N * 4^L) where L = max word length
Space Complexity: O(total chars in words) for Trie
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store complete word at end node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r: int, c: int, node: TrieNode) -> None:
            ch = board[r][c]
            if ch not in node.children:
                return

            next_node = node.children[ch]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # deduplicate

            board[r][c] = '#'  # mark visited
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
            board[r][c] = ch  # restore

            # Prune empty trie nodes
            if not next_node.children:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print(sol.findWords(board, words))  # ["eat","oath"]
