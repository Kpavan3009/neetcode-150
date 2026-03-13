"""
Problem: Encode and Decode Strings (LeetCode #271 / NeetCode)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can strings contain any character including '#', digits, spaces? (Yes)
- Can strings be empty? (Yes)
- Can the list be empty? (Yes)
- Is there a character guaranteed not to appear in strings? (No, assume any char possible)

APPROACH / PSEUDOCODE:
- Encode: for each string, prepend its length followed by a '#' delimiter
  e.g., ["hello", "world"] → "5#hello5#world"
- Decode: read until '#' to get length, then read exactly that many chars as next string
- Using length prefix makes it unambiguous regardless of string content

Time Complexity: O(n) for both encode and decode, where n = total chars
Space Complexity: O(n) for the encoded string / decoded list
"""

from typing import List


def encode(strs: List[str]) -> str:
    result = []
    for s in strs:
        result.append(f"{len(s)}#{s}")
    return "".join(result)


def decode(s: str) -> List[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        result.append(s[j + 1: j + 1 + length])
        i = j + 1 + length
    return result


# Test cases
if __name__ == "__main__":
    strs = ["hello", "world"]
    encoded = encode(strs)
    print(encoded)           # "5#hello5#world"
    print(decode(encoded))   # ["hello", "world"]

    strs2 = ["we", "say", ":", "yes", "#", "no"]
    encoded2 = encode(strs2)
    print(decode(encoded2))  # ["we", "say", ":", "yes", "#", "no"]
