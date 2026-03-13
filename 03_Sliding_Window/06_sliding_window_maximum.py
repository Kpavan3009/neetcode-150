"""
Problem: Sliding Window Maximum (LeetCode #239)
Difficulty: Hard

CLARIFYING QUESTIONS:
- What if k > len(nums)? (Assume k is always valid: 1 <= k <= len(nums))
- Can nums contain negative numbers? (Yes)
- What if the array has only one element? (Return that element)

APPROACH / PSEUDOCODE:
- Use a monotonic decreasing deque (stores indices)
- For each new element:
    - Remove indices from back of deque if current element >= nums[deque[-1]]
      (those can never be the maximum for any future window)
    - Add current index to back
    - Remove front of deque if it's out of current window
    - Once we've processed at least k elements, record deque front as window max

Time Complexity: O(n) - each element added/removed from deque at most once
Space Complexity: O(k) - deque holds at most k indices
"""

from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = deque()  # stores indices, decreasing order of values
    result = []

    for i in range(len(nums)):
        # Remove elements out of current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Maintain decreasing monotonic deque
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        dq.append(i)

        # Start recording results once first window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Test cases
if __name__ == "__main__":
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
    print(maxSlidingWindow([1], 1))                    # [1]
