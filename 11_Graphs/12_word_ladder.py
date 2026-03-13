"""
Problem: Word Ladder (LeetCode #127)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Change one letter at a time, each intermediate word must be in wordList? (Yes)
- Return length of shortest transformation sequence? (Yes, including begin and end)
- Return 0 if no path? (Yes)
- beginWord included in wordList? (Not necessarily)

APPROACH / PSEUDOCODE:
- BFS from beginWord (shortest path = fewest transformations)
- At each step, try changing each character to a-z
- If new word is in word set and not visited → add to queue
- Return level count when endWord is reached

Time Complexity: O(M^2 * N) where M = word length, N = wordList size
Space Complexity: O(M^2 * N)
"""

from collections import deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])  # (word, path_length)
    visited = {beginWord}

    while queue:
        word, length = queue.popleft()

        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + ch + word[i+1:]
                if new_word == endWord:
                    return length + 1
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, length + 1))

    return 0


# Test cases
if __name__ == "__main__":
    print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # 5
    print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))        # 0
