"""
Shared ListNode definition and helper functions used across Linked List solutions.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(head):
    """Convert linked list to Python list for easy testing."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(vals):
    """Convert Python list to linked list."""
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next
