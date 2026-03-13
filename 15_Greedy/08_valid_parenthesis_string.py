"""
Problem: Valid Parenthesis String (LeetCode #678)
Difficulty: Medium

CLARIFYING QUESTIONS:
- '*' can be '(', ')' or empty? (Yes)
- Empty string is valid? (Yes)

APPROACH / PSEUDOCODE:
- Track range of possible "open bracket counts" [lo, hi]
- lo = minimum possible open count (treat '*' as ')')
- hi = maximum possible open count (treat '*' as '(')
- For each char:
    '(' → lo++, hi++
    ')' → lo--, hi--
    '*' → lo--, hi++  (try as ')' for lo, as '(' for hi)
- If hi < 0 → too many ')' → False
- Clamp lo to 0 (can't have negative open count)
- At end, valid if lo == 0

Time Complexity: O(n)
Space Complexity: O(1)
"""


def checkValidString(s: str) -> bool:
    lo = hi = 0  # range of possible open bracket counts

    for ch in s:
        if ch == '(':
            lo += 1
            hi += 1
        elif ch == ')':
            lo -= 1
            hi -= 1
        else:  # '*'
            lo -= 1  # treat as ')'
            hi += 1  # treat as '('

        if hi < 0:
            return False  # too many ')'

        lo = max(lo, 0)  # can't have negative open count

    return lo == 0


# Test cases
if __name__ == "__main__":
    print(checkValidString("()"))         # True
    print(checkValidString("(*)"))        # True
    print(checkValidString("(*))"))       # True
    print(checkValidString("(*)("))       # False
