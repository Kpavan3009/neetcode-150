"""
Problem: Design Add and Search Words Data Structure (LeetCode #211)
Difficulty: Medium

CLARIFYING QUESTIONS:
- The '.' character matches any single letter? (Yes)
- Only lowercase letters and '.'? (Yes)
- Multiple '.' can appear in a word? (Yes)

APPROACH / PSEUDOCODE:
- Same Trie structure as basic Trie
- addWord: standard trie insert
- search: DFS through trie; when '.' encountered → try all children recursively
- If char found → advance normally; if '.' → branch to all children

Time Complexity: addWord O(m), search O(m) average, O(m * 26^m) worst with many dots
Space Complexity: O(m * n) for n words of length m
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(idx: int, node: TrieNode) -> bool:
            if idx == len(word):
                return node.end_of_word

            ch = word[idx]
            if ch == '.':
                for child in node.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(idx + 1, node.children[ch])

        return dfs(0, self.root)


# Test cases
if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))  # False
    print(wd.search("bad"))  # True
    print(wd.search(".ad"))  # True
    print(wd.search("b.."))  # True
