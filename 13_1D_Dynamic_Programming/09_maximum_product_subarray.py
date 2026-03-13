"""
Problem: Maximum Product Subarray (LeetCode #152)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can array contain zeros and negative numbers? (Yes)
- Return the product (not indices)? (Yes)
- Minimum length 1? (Yes)

APPROACH / PSEUDOCODE:
- Track both max_prod and min_prod at each position
  (min needed because negative * negative = positive)
- At each num: new_max = max(num, num*prev_max, num*prev_min)
               new_min = min(num, num*prev_max, num*prev_min)
- Update global maximum

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def maxProduct(nums: List[int]) -> int:
    result = max(nums)
    curr_min = curr_max = 1

    for num in nums:
        if num == 0:
            curr_min = curr_max = 1
            continue
        candidates = (num, num * curr_max, num * curr_min)
        curr_max = max(candidates)
        curr_min = min(candidates)
        result = max(result, curr_max)

    return result


# Test cases
if __name__ == "__main__":
    print(maxProduct([2,3,-2,4]))   # 6 ([2,3])
    print(maxProduct([-2,0,-1]))    # 0
    print(maxProduct([-2,3,-4]))    # 24
