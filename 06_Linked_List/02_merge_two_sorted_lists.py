"""
Problem: Merge Two Sorted Lists (LeetCode #21)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Can either list be empty? (Yes)
- Are both lists sorted in ascending order? (Yes)
- Should I create a new list or modify in place? (Either is fine)

APPROACH / PSEUDOCODE:
- Use a dummy node to simplify edge cases
- Compare heads of both lists, attach the smaller one to result
- Advance the pointer in the list we took from
- When one list is exhausted, append remaining of the other

Time Complexity: O(m + n)
Space Complexity: O(1) - modifying links, not creating new nodes
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 if list1 else list2

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

    l1 = from_list([1,2,4])
    l2 = from_list([1,3,4])
    print(to_list(mergeTwoLists(l1, l2)))  # [1,1,2,3,4,4]
    print(to_list(mergeTwoLists(None, None)))  # []
