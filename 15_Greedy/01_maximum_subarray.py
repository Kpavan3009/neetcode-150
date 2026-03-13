"""
Problem: Maximum Subarray (LeetCode #53)
Difficulty: Medium

CLARIFYING QUESTIONS:
- At least one element in array? (Yes)
- Can contain negative numbers? (Yes)
- Return the sum (not the subarray)? (Yes)

APPROACH / PSEUDOCODE:
- Kadane's Algorithm: greedy + DP
- Track current sum; if it goes negative, reset to 0 (start fresh)
- At each step: current_sum = max(num, current_sum + num)
  (either extend current subarray or start new one at current element)
- Track maximum seen

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Test cases
if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6 ([4,-1,2,1])
    print(maxSubArray([1]))                        # 1
    print(maxSubArray([5,4,-1,7,8]))               # 23
