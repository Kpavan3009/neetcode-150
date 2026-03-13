"""
Problem: Reverse Linked List (LeetCode #206)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Can the list be empty? (Yes, return None)
- Should I do it iteratively or recursively? (Either works, iterative is O(1) space)
- Is it a singly linked list? (Yes)

APPROACH / PSEUDOCODE:
- Iterative approach: maintain prev pointer
- For each node: save next, point current's next to prev, advance prev and current
- Return prev (new head) when current becomes None

Time Complexity: O(n)
Space Complexity: O(1) iterative, O(n) recursive
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# Recursive approach
def reverseList_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    new_head = reverseList_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# Helper functions for testing
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def from_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    print(to_list(reverseList(from_list([1,2,3,4,5]))))  # [5,4,3,2,1]
    print(to_list(reverseList(from_list([1,2]))))         # [2,1]
    print(to_list(reverseList(None)))                     # []
