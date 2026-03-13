"""
Problem: Reverse Nodes in k-Group (LeetCode #25)
Difficulty: Hard

CLARIFYING QUESTIONS:
- If remaining nodes < k, leave them as is? (Yes)
- k is always positive? (Yes, 1 <= k <= list length)
- Should we modify in place? (Yes)

APPROACH / PSEUDOCODE:
- Use a dummy node before head
- For each group of k nodes:
    - Check if there are k nodes remaining (if not, stop)
    - Reverse k nodes
    - Connect reversed group back to main list
    - Advance to next group
- Return dummy.next

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        # Check if k nodes exist ahead
        kth = get_kth(group_prev, k)
        if not kth:
            break

        group_next = kth.next

        # Reverse the group
        prev = group_next
        curr = group_prev.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Reconnect
        tmp = group_prev.next   # original first of group (now last)
        group_prev.next = kth   # connect to new first of group (was kth)
        group_prev = tmp        # advance group_prev to new tail of reversed group

    return dummy.next


def get_kth(curr: ListNode, k: int) -> Optional[ListNode]:
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


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

    print(to_list(reverseKGroup(from_list([1,2,3,4,5]), 2)))  # [2,1,4,3,5]
    print(to_list(reverseKGroup(from_list([1,2,3,4,5]), 3)))  # [3,2,1,4,5]
