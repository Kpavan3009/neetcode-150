"""
Problem: Reorder List (LeetCode #143)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Reorder in place? (Yes, modify the list)
- What if list has 1 or 2 nodes? (No change needed)
- Is it: L0 → Ln → L1 → Ln-1 → ...? (Yes)

APPROACH / PSEUDOCODE:
- Step 1: Find middle of list using slow/fast pointers
- Step 2: Reverse the second half of the list
- Step 3: Merge the two halves by alternating nodes

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return

    # Step 1: Find middle (slow/fast pointer)
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    second = slow.next
    slow.next = None  # Cut list in half
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev  # Head of reversed second half

    # Step 3: Merge two halves
    first = head
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


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

    l = from_list([1,2,3,4])
    reorderList(l)
    print(to_list(l))  # [1,4,2,3]

    l2 = from_list([1,2,3,4,5])
    reorderList(l2)
    print(to_list(l2))  # [1,5,2,4,3]
