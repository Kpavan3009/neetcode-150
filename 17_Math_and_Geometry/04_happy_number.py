"""
Problem: Happy Number (LeetCode #202)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Sum of squares of digits; repeat until 1 or cycle? (Yes)
- Return True if eventually reaches 1? (Yes)

APPROACH / PSEUDOCODE:
- Floyd's cycle detection (slow/fast pointers) on the sequence
- Or: use a set to detect cycle (simpler)
- If we ever reach 1 → happy; if we enter a cycle not containing 1 → not happy

Time Complexity: O(log n) per step, total O(log n * log(log n))
Space Complexity: O(1) with Floyd's, O(log n) with set
"""


def isHappy(n: int) -> bool:
    def get_next(num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    # Floyd's cycle detection
    slow = n
    fast = get_next(n)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1


# Set approach (simpler but O(log n) space):
def isHappy_set(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1


# Test cases
if __name__ == "__main__":
    print(isHappy(19))  # True (1^2 + 9^2 = 82, 8^2+2^2=68, ... → 1)
    print(isHappy(2))   # False
