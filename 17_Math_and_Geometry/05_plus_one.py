"""
Problem: Plus One (LeetCode #66)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Array represents a large integer (most significant digit first)? (Yes)
- No leading zeros (except the number 0)? (Yes)
- Add 1 to the integer? (Yes)

APPROACH / PSEUDOCODE:
- Traverse from right to left
- If digit + 1 < 10 → increment and return (no carry)
- If digit is 9 → set to 0 and carry over
- If all digits were 9 → prepend 1 (e.g., [9,9] → [1,0,0])

Time Complexity: O(n)
Space Complexity: O(1) in-place
"""

from typing import List


def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # carry over

    # All digits were 9 → need extra digit
    return [1] + digits


# Test cases
if __name__ == "__main__":
    print(plusOne([1,2,3]))  # [1,2,4]
    print(plusOne([4,3,2,1]))  # [4,3,2,2]
    print(plusOne([9]))      # [1,0]
    print(plusOne([9,9,9]))  # [1,0,0,0]
