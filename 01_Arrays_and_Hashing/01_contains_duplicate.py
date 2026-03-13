"""
Problem: Contains Duplicate (LeetCode #217)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Can the array be empty? (Yes, return False)
- Can nums contain negative integers? (Yes)
- What's the range of values? (Assume standard int range)
- Should I handle None input? (Assume valid input)

APPROACH / PSEUDOCODE:
- Use a hash set to track seen numbers
- Iterate through the array
- If current number already in set → duplicate found, return True
- Otherwise add to set
- Return False if no duplicate found

Time Complexity: O(n) - single pass through array
Space Complexity: O(n) - hash set stores up to n elements
"""

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Alternative one-liner (same complexity):
# return len(nums) != len(set(nums))


# Test cases
if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))   # True
    print(containsDuplicate([1, 2, 3, 4]))   # False
    print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
