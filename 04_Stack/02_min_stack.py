"""
Problem: Min Stack (LeetCode #155)
Difficulty: Medium

CLARIFYING QUESTIONS:
- All operations must be O(1) time? (Yes)
- What if getMin() or top() is called on empty stack? (Assume always valid calls)
- Can values be negative? (Yes)

APPROACH / PSEUDOCODE:
- Maintain two stacks: main stack and a min_stack
- min_stack tracks the minimum at each state
- On push(val): push to main stack; push min(val, min_stack.top()) to min_stack
- On pop(): pop from both stacks
- getMin(): return top of min_stack
- top(): return top of main stack

Time Complexity: O(1) for all operations
Space Complexity: O(n) - two stacks
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Each entry tracks current min

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Test cases
if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())  # -3
    ms.pop()
    print(ms.top())     # 0
    print(ms.getMin())  # -2
