"""
Problem: Remove Nth Node From End of List (LeetCode #19)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Is n always valid (1 <= n <= list length)? (Yes)
- Can we do it in one pass? (Yes, that's the optimal approach)
- What if removing the head? (Handle with dummy node)

APPROACH / PSEUDOCODE:
- Use two pointers: fast and slow, both starting at dummy node
- Move fast pointer n+1 steps ahead
- Move both pointers until fast reaches end
- slow.next is the node to delete → slow.next = slow.next.next
- Dummy node handles edge case of removing head

Time Complexity: O(n) - single pass
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast hits end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the target node
    slow.next = slow.next.next

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

    print(to_list(removeNthFromEnd(from_list([1,2,3,4,5]), 2)))  # [1,2,3,5]
    print(to_list(removeNthFromEnd(from_list([1]), 1)))           # []
    print(to_list(removeNthFromEnd(from_list([1,2]), 1)))         # [1]
