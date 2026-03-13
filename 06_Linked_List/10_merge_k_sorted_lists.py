"""
Problem: Merge K Sorted Lists (LeetCode #23)
Difficulty: Hard

CLARIFYING QUESTIONS:
- Can k be 0 (empty input)? (Yes, return None)
- Can individual lists be empty/None? (Yes)
- Are all lists sorted in ascending order? (Yes)

APPROACH / PSEUDOCODE:
- Use a min-heap to always get the smallest current element across all lists
- Push (value, index, node) for each list's head
- Pop smallest, add to result, push its next node if exists
- Use index as tiebreaker to avoid comparing ListNode objects

Time Complexity: O(N log k) where N = total nodes, k = number of lists
Space Complexity: O(k) - heap size bounded by k
"""

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []

    # Initialize heap with head of each non-empty list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# Test cases
if __name__ == "__main__":
    def from_list(vals):
        dummy = ListNode(0)
        curr = dummy
        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    def to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    lists = [from_list([1,4,5]), from_list([1,3,4]), from_list([2,6])]
    print(to_list(mergeKLists(lists)))  # [1,1,2,3,4,4,5,6]
