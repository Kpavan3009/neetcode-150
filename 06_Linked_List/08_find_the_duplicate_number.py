"""
Problem: Find the Duplicate Number (LeetCode #287)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Array has n+1 integers in range [1, n]? (Yes)
- There's exactly one duplicate (but can appear more than twice)? (Yes, one duplicate value)
- Cannot modify the array? (Yes)
- Must use O(1) extra space? (Yes)

APPROACH / PSEUDOCODE:
- Treat array as a linked list where index → nums[index]
- Since there's a duplicate value, two indices point to the same next node → cycle!
- Apply Floyd's Cycle Detection:
    Phase 1: Find intersection point inside cycle (slow/fast pointers)
    Phase 2: Find cycle entry point (= duplicate number) using two slow pointers
        - Reset one pointer to start, keep other at intersection
        - Both move 1 step until they meet → entry = duplicate

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def findDuplicate(nums: List[int]) -> int:
    # Phase 1: Detect cycle
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # Phase 2: Find cycle entry (= duplicate)
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# Test cases
if __name__ == "__main__":
    print(findDuplicate([1,3,4,2,2]))  # 2
    print(findDuplicate([3,1,3,4,2]))  # 3
    print(findDuplicate([1,1]))        # 1
