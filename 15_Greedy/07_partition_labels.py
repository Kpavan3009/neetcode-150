"""
Problem: Partition Labels (LeetCode #763)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Each letter appears in at most one part? (Yes, as few parts as possible)
- Return list of part sizes? (Yes)
- String contains only lowercase letters? (Yes)

APPROACH / PSEUDOCODE:
- Record the last occurrence of each character
- Greedy: expand current partition to include last occurrence of each char seen so far
- When current index reaches end of current partition → that's a cut point

Time Complexity: O(n)
Space Complexity: O(1) - at most 26 chars
"""

from typing import List


def partitionLabels(s: str) -> List[int]:
    last = {ch: i for i, ch in enumerate(s)}  # last occurrence of each char

    result = []
    start = 0
    end = 0

    for i, ch in enumerate(s):
        end = max(end, last[ch])  # extend partition to last occurrence of current char

        if i == end:  # reached end of current partition
            result.append(end - start + 1)
            start = i + 1

    return result


# Test cases
if __name__ == "__main__":
    print(partitionLabels("ababcbacadefegdehijhklij"))  # [9, 7, 8]
    print(partitionLabels("eccbbbbdec"))                 # [10]
