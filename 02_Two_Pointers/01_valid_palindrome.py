"""
Problem: Valid Palindrome (LeetCode #125)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Should we ignore non-alphanumeric characters? (Yes)
- Is it case-sensitive? (No, case-insensitive)
- Is an empty string a palindrome? (Yes)
- What counts as alphanumeric? (Letters a-z and digits 0-9)

APPROACH / PSEUDOCODE:
- Use two pointers: left at start, right at end
- Skip non-alphanumeric characters on both sides
- Compare characters (case-insensitive) at both pointers
- If mismatch → not a palindrome
- Move pointers inward and repeat
- Return True if pointers meet/cross

Time Complexity: O(n) - single pass through string
Space Complexity: O(1) - only two pointer variables
"""


def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Test cases
if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(isPalindrome("race a car"))                       # False
    print(isPalindrome(" "))                                # True
