"""
Problem: Merge Triplets to Form Target Triplet (LeetCode #1899)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Merge = take element-wise maximum of two triplets? (Yes)
- Can use each triplet as many times as we want? (Yes, but operations are all merging)
- Return True if target triplet achievable? (Yes)

APPROACH / PSEUDOCODE:
- Key insight: discard any triplet with a component GREATER than target's component
  (such a triplet would corrupt the target if merged)
- From remaining valid triplets, check if we can achieve each target component
- If a valid triplet has component equal to target component → that component is achievable
- All 3 components must be achievable

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    # Track which target components we can achieve
    achieved = set()

    for a, b, c in triplets:
        ta, tb, tc = target
        # Discard invalid triplets (any component exceeds target)
        if a > ta or b > tb or c > tc:
            continue
        # Check which target components this triplet achieves
        if a == ta:
            achieved.add(0)
        if b == tb:
            achieved.add(1)
        if c == tc:
            achieved.add(2)

    return len(achieved) == 3


# Test cases
if __name__ == "__main__":
    print(mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))  # True
    print(mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]))           # False
    print(mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))  # True
