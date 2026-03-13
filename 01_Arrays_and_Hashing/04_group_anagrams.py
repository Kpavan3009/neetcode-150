"""
Problem: Group Anagrams (LeetCode #49)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can the input list be empty? (Yes, return empty list)
- Are strings all lowercase? (Yes, lowercase English letters)
- Can strings be empty? (Yes, empty string groups with other empty strings)
- Is output order important? (No)

APPROACH / PSEUDOCODE:
- Use a hash map: sorted_word -> list of anagrams
- For each word, sort its characters to get a canonical key
- All anagrams will produce the same sorted key
- Group words by their sorted key
- Return all groups as a list of lists

Time Complexity: O(n * k log k) where n = number of words, k = max word length
Space Complexity: O(n * k) - storing all words in the hash map
"""

from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())


# Alternative: use character count as key (avoids sorting)
def groupAnagrams_v2(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(word)
    return list(groups.values())
# v2 Time: O(n * k), Space: O(n * k)


# Test cases
if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["eat","tea","ate"],["tan","nat"],["bat"]]
    print(groupAnagrams([""]))   # [[""]]
    print(groupAnagrams(["a"]))  # [["a"]]
