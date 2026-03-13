"""
Problem: Single Number (LeetCode #136)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Every element appears twice except one? (Yes)
- Must use O(1) space? (Yes)
- Can the input be empty? (No, at least one element)

APPROACH / PSEUDOCODE:
- XOR all numbers together
- a XOR a = 0 (cancel pairs)
- a XOR 0 = a (single element remains)
- Order doesn't matter (XOR is commutative and associative)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


# Test cases
if __name__ == "__main__":
    print(singleNumber([2,2,1]))       # 1
    print(singleNumber([4,1,2,1,2]))   # 4
    print(singleNumber([1]))           # 1
