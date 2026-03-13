"""
Problem: Valid Parentheses (LeetCode #20)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Only these three types: (), [], {}? (Yes)
- Can the string be empty? (Yes, return True)
- Can string contain other characters? (No, only brackets)

APPROACH / PSEUDOCODE:
- Use a stack
- For each character:
    - If opening bracket → push to stack
    - If closing bracket → check if stack top matches
        - If mismatch or stack empty → return False
        - Otherwise pop from stack
- At end, return True only if stack is empty

Time Complexity: O(n)
Space Complexity: O(n) - stack in worst case holds all chars
"""


def isValid(s: str) -> bool:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    return len(stack) == 0


# Test cases
if __name__ == "__main__":
    print(isValid("()"))        # True
    print(isValid("()[]{}"))    # True
    print(isValid("(]"))        # False
    print(isValid("([)]"))      # False
    print(isValid("{[]}"))      # True
