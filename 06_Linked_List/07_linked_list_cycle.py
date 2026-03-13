"""
Problem: Linked List Cycle (LeetCode #141)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Return True if cycle exists, False otherwise? (Yes)
- Can I modify the list? (Prefer not to)
- What if list is empty? (Return False)

APPROACH / PSEUDOCODE:
- Floyd's Cycle Detection (Tortoise and Hare)
- slow pointer moves 1 step, fast pointer moves 2 steps
- If they ever meet → cycle exists
- If fast reaches None → no cycle

Time Complexity: O(n)
Space Complexity: O(1) - only two pointers (vs O(n) with a hash set)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


# Test cases
if __name__ == "__main__":
    # Create cycle: 3 → 2 → 0 → -4 → back to 2
    nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[3].next = nodes[1]  # cycle
    print(hasCycle(nodes[0]))  # True

    # No cycle: 1 → 2
    n1, n2 = ListNode(1), ListNode(2)
    n1.next = n2
    print(hasCycle(n1))  # False
