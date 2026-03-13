"""
Problem: Longest Increasing Subsequence (LeetCode #300)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Strictly increasing? (Yes)
- Not necessarily contiguous? (Correct, it's a subsequence)
- Return the length? (Yes)

APPROACH 1 - DP: O(n^2)
- dp[i] = LIS ending at index i
- dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])

APPROACH 2 - Patience Sorting (optimal): O(n log n)
- Maintain an array 'tails' where tails[i] = smallest tail of all IS of length i+1
- For each num: binary search for its position in tails
    - If larger than all → extend; else replace

Time Complexity: O(n log n) with patience sorting
Space Complexity: O(n)
"""

from typing import List
import bisect


def lengthOfLIS(nums: List[int]) -> int:
    tails = []  # tails[i] = smallest tail element for IS of length i+1

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


# O(n^2) DP for reference
def lengthOfLIS_dp(nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)


# Test cases
if __name__ == "__main__":
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))  # 4 [2,3,7,101]
    print(lengthOfLIS([0,1,0,3,2,3]))          # 4
    print(lengthOfLIS([7,7,7,7,7,7,7]))        # 1
