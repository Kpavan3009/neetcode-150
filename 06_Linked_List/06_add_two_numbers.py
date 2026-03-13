"""
Problem: Add Two Numbers (LeetCode #2)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Digits stored in reverse order (least significant first)? (Yes)
- Can either number be 0? (Yes)
- No leading zeros except for the number 0 itself? (Yes)

APPROACH / PSEUDOCODE:
- Simulate addition digit by digit with carry
- Use a dummy head to simplify result list construction
- At each step: sum = l1.val + l2.val + carry
- New node value = sum % 10, carry = sum // 10
- Continue until both lists are exhausted AND carry is 0

Time Complexity: O(max(m, n)) where m, n are lengths of lists
Space Complexity: O(max(m, n)) - result list length
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

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

    # 342 + 465 = 807 → [7,0,8]
    print(to_list(addTwoNumbers(from_list([2,4,3]), from_list([5,6,4]))))
    # 0 + 0 = 0 → [0]
    print(to_list(addTwoNumbers(from_list([0]), from_list([0]))))
