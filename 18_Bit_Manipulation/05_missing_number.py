"""
Problem: Missing Number (LeetCode #268)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Array contains n distinct numbers in range [0, n]? (Yes)
- Exactly one number missing? (Yes)
- Return the missing number? (Yes)

APPROACH 1 - XOR: O(n) time, O(1) space
- XOR all indices 0..n with all values in array
- Pairs cancel out, leaving the missing number

APPROACH 2 - Math: O(n) time, O(1) space
- Expected sum = n*(n+1)/2; actual sum = sum(nums)
- Missing = expected - actual

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)


# XOR approach (avoids potential overflow in other languages):
def missingNumber_xor(nums: List[int]) -> int:
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result


# Test cases
if __name__ == "__main__":
    print(missingNumber([3,0,1]))     # 2
    print(missingNumber([0,1]))       # 2
    print(missingNumber([9,6,4,2,3,5,7,0,1]))  # 8
