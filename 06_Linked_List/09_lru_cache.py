"""
Problem: LRU Cache (LeetCode #146)
Difficulty: Medium

CLARIFYING QUESTIONS:
- What happens when capacity is exceeded? (Evict least recently used)
- get() and put() must be O(1)? (Yes)
- What if we put() an existing key? (Update the value and make it most recently used)
- get() returns -1 if key not found? (Yes)

APPROACH / PSEUDOCODE:
- Use a doubly linked list + hash map
- Hash map: key → node (for O(1) lookup)
- Doubly linked list: tracks order from LRU (left/head) to MRU (right/tail)
- get(): look up node, move to right (MRU), return value
- put(): if exists → update and move to MRU; if new → add to MRU;
         if over capacity → remove from LRU (leftmost) and map

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
"""


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head (LRU side) and tail (MRU side)
        self.left = Node()   # LRU sentinel
        self.right = Node()  # MRU sentinel
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_mru(self, node: Node) -> None:
        """Insert node just before right sentinel (MRU position)."""
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_mru(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._insert_mru(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next  # evict LRU
            self._remove(lru)
            del self.cache[lru.key]


# Test cases
if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))    # 1
    lru.put(3, 3)        # evicts key 2
    print(lru.get(2))    # -1
    lru.put(4, 4)        # evicts key 1
    print(lru.get(1))    # -1
    print(lru.get(3))    # 3
    print(lru.get(4))    # 4
