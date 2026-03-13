"""
Problem: Longest Consecutive Sequence (LeetCode #128)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can the array be empty? (Yes, return 0)
- Can it contain duplicates? (Yes, ignore them)
- Can it have negative numbers? (Yes)
- Must the algorithm run in O(n)? (Yes, that's the goal)

APPROACH / PSEUDOCODE:
- Convert array to a hash set for O(1) lookups
- For each number, only start counting if it's the beginning of a sequence
  (i.e., num - 1 is NOT in the set)
- From each sequence start, count consecutive numbers (num+1, num+2, ...)
- Track and return the maximum streak length

Time Complexity: O(n) - each element is visited at most twice
Space Complexity: O(n) - hash set
"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start a sequence from its beginning
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            longest = max(longest, streak)

    return longest


# Test cases
if __name__ == "__main__":
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4 → [1,2,3,4]
    print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(longestConsecutive([]))  # 0
