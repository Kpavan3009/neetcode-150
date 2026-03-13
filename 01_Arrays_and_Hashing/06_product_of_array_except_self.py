"""
Problem: Product of Array Except Self (LeetCode #238)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can the array contain zeros? (Yes)
- Can it contain negative numbers? (Yes)
- Can I use division? (No, solve without division)
- What's the minimum array length? (At least 2)
- Should output array count as extra space? (No, output doesn't count)

APPROACH / PSEUDOCODE:
- For each index i, result[i] = product of all elements to left * product of all elements to right
- Pass 1 (left to right): compute prefix products, store in result array
- Pass 2 (right to left): multiply by suffix products on the fly using a running variable
- No extra array needed beyond the output

Time Complexity: O(n) - two passes
Space Complexity: O(1) - output array doesn't count as extra space
"""

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    # Forward pass: result[i] = product of all elements before i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Backward pass: multiply by product of all elements after i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# Test cases
if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))      # [24, 12, 8, 6]
    print(productExceptSelf([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]
