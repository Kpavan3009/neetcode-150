"""
Problem: Median of Two Sorted Arrays (LeetCode #4)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Must run in O(log(m+n)) time? (Yes, that's the challenge)
- Can either array be empty? (Yes)
- Are arrays sorted? (Yes)

APPROACH / PSEUDOCODE:
- Binary search on the smaller array to find the correct partition
- Partition both arrays such that left half has (m+n+1)//2 elements
- Partition is valid when: maxLeft1 <= minRight2 AND maxLeft2 <= minRight1
- If maxLeft1 > minRight2 → move partition left in nums1
- If maxLeft2 > minRight1 → move partition right in nums1
- Median = average of max-left and min-right for even total length
         = max-left for odd total length

Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
"""

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    half = (m + n + 1) // 2
    left, right = 0, m

    while left <= right:
        i = left + (right - left) // 2  # partition index for nums1
        j = half - i                     # partition index for nums2

        maxLeft1 = nums1[i - 1] if i > 0 else float('-inf')
        minRight1 = nums1[i] if i < m else float('inf')
        maxLeft2 = nums2[j - 1] if j > 0 else float('-inf')
        minRight2 = nums2[j] if j < n else float('inf')

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Valid partition found
            if (m + n) % 2 == 1:
                return float(max(maxLeft1, maxLeft2))
            else:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
        elif maxLeft1 > minRight2:
            right = i - 1
        else:
            left = i + 1

    return 0.0


# Test cases
if __name__ == "__main__":
    print(findMedianSortedArrays([1,3], [2]))       # 2.0
    print(findMedianSortedArrays([1,2], [3,4]))     # 2.5
