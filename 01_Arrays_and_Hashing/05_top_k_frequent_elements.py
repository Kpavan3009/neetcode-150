"""
Problem: Top K Frequent Elements (LeetCode #347)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Is k always valid (1 <= k <= number of unique elements)? (Yes)
- Can there be ties in frequency? (Yes, any valid answer is accepted)
- Can array be empty? (No, guaranteed at least 1 element)
- Should the result be in any particular order? (No)

APPROACH / PSEUDOCODE:
- Count frequency of each element using a hash map
- Use bucket sort: create array of size n+1 where index = frequency
- Place each element into its frequency bucket
- Iterate buckets from high to low, collect elements until we have k
- This avoids sorting and achieves O(n) time

Time Complexity: O(n) - bucket sort approach
Space Complexity: O(n) - frequency map + buckets
"""

from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)

    # Bucket sort: index = frequency, value = list of nums with that freq
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result


# Alternative using heap (O(n log k)):
# import heapq
# def topKFrequent_heap(nums, k):
#     count = Counter(nums)
#     return heapq.nlargest(k, count.keys(), key=count.get)


# Test cases
if __name__ == "__main__":
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(topKFrequent([1], 1))                   # [1]
