"""
Problem: Valid Anagram (LeetCode #242)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Are the strings always lowercase? (Assume yes, lowercase English letters)
- Can strings be empty? (Yes, two empty strings are anagrams)
- Is the comparison case-sensitive? (Yes)
- Unicode characters? (Assume only lowercase English letters)

APPROACH / PSEUDOCODE:
- If lengths differ → not anagram, return False
- Count character frequencies in s using a hash map
- Decrement counts for each character in t
- If any count goes negative → t has extra char, return False
- If all counts are zero → valid anagram

Time Complexity: O(n) where n is length of strings
Space Complexity: O(1) - at most 26 keys in the map (fixed alphabet)
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True


# Alternative using Counter:
# from collections import Counter
# return Counter(s) == Counter(t)


# Test cases
if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))  # True
    print(isAnagram("rat", "car"))          # False
    print(isAnagram("", ""))               # True
