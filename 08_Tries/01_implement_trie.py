"""
Problem: Implement Trie (Prefix Tree) (LeetCode #208)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Only lowercase English letters? (Yes)
- insert, search, startsWith all needed? (Yes)
- search: returns True only if FULL word exists? (Yes)
- startsWith: returns True if any word has this prefix? (Yes)

APPROACH / PSEUDOCODE:
- Each TrieNode has: children dict (char → TrieNode) and end_of_word flag
- insert: traverse/create nodes for each char; mark last node as end_of_word
- search: traverse nodes; return True only if all chars found AND end_of_word
- startsWith: traverse nodes; return True if all chars found

Time Complexity: O(m) for all operations, m = word length
Space Complexity: O(m * n) total for n words of average length m
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True


# Test cases
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    # True
    print(trie.search("app"))      # False
    print(trie.startsWith("app"))  # True
    trie.insert("app")
    print(trie.search("app"))      # True
