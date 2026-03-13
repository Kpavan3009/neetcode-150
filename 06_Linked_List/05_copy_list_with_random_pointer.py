"""
Problem: Copy List with Random Pointer (LeetCode #138)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Random pointer can point to any node or None? (Yes)
- Should I deep copy (new nodes for everything)? (Yes)
- Can the list be empty? (Yes, return None)

APPROACH / PSEUDOCODE:
- Use a hash map: original_node → copied_node
- First pass: create all copied nodes and store in map
- Second pass: assign next and random pointers using the map

Time Complexity: O(n)
Space Complexity: O(n) - hash map
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    old_to_new = {}

    # First pass: create all new nodes
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # Second pass: assign pointers
    curr = head
    while curr:
        if curr.next:
            old_to_new[curr].next = old_to_new[curr.next]
        if curr.random:
            old_to_new[curr].random = old_to_new[curr.random]
        curr = curr.next

    return old_to_new[head]


# Test cases
if __name__ == "__main__":
    # Build: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[0].random = None
    nodes[1].random = nodes[0]
    nodes[2].random = nodes[4]
    nodes[3].random = nodes[2]
    nodes[4].random = nodes[0]

    copied = copyRandomList(nodes[0])
    curr = copied
    while curr:
        rand_val = curr.random.val if curr.random else None
        print(f"val={curr.val}, random={rand_val}")
        curr = curr.next
