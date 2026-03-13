"""
Problem: Evaluate Reverse Polish Notation (LeetCode #150)
Difficulty: Medium

CLARIFYING QUESTIONS:
- What operators are supported? (+, -, *, /)
- Integer division truncates toward zero? (Yes)
- Is the input always valid (no division by zero)? (Yes)
- Can operands be negative? (Yes)

APPROACH / PSEUDOCODE:
- Use a stack for operands
- For each token:
    - If it's a number → push to stack
    - If it's an operator → pop two values, apply operator, push result
      (note: pop order matters: second = first popped, first = second popped)
- Return stack top as final result

Time Complexity: O(n) - process each token once
Space Complexity: O(n) - stack
"""

from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    ops = {'+', '-', '*', '/'}

    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                # Python's // rounds toward negative infinity, need truncation toward 0
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


# Test cases
if __name__ == "__main__":
    print(evalRPN(["2","1","+","3","*"]))            # 9  → (2+1)*3
    print(evalRPN(["4","13","5","/","+"]))            # 6  → 4+(13/5)
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22
