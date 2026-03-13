"""
Problem: Hand of Straights (LeetCode #846)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Rearrange into groups of consecutive cards of size groupSize? (Yes)
- Return True if possible? (Yes)
- If hand size not divisible by groupSize → False? (Yes)

APPROACH / PSEUDOCODE:
- Use a sorted frequency map
- Process cards in order from smallest to largest
- For each group starting at the smallest available card:
    - Consume groupSize consecutive cards
    - If any card in sequence unavailable → return False

Time Complexity: O(n log n) - sorting
Space Complexity: O(n)
"""

from typing import List
from collections import Counter


def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    count = Counter(hand)

    for card in sorted(count):
        freq = count[card]
        if freq == 0:
            continue
        for next_card in range(card, card + groupSize):
            if count[next_card] < freq:
                return False
            count[next_card] -= freq

    return True


# Test cases
if __name__ == "__main__":
    print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # True
    print(isNStraightHand([1,2,3,4,5], 4))            # False
