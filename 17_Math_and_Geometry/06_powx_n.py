"""
Problem: Pow(x, n) (LeetCode #50)
Difficulty: Medium

CLARIFYING QUESTIONS:
- n can be negative? (Yes, x^-n = 1/x^n)
- x can be negative? (Yes)
- Integer overflow? (Use Python's arbitrary precision)

APPROACH / PSEUDOCODE:
- Fast exponentiation (binary exponentiation):
    - If n is even: x^n = (x^2)^(n/2)
    - If n is odd: x^n = x * x^(n-1)
- Handle negative n by inverting x

Time Complexity: O(log n)
Space Complexity: O(log n) recursive, O(1) iterative
"""


def myPow(x: float, n: int) -> float:
    def fast_pow(base: float, exp: int) -> float:
        if exp == 0:
            return 1.0
        if exp % 2 == 0:
            half = fast_pow(base, exp // 2)
            return half * half
        else:
            return base * fast_pow(base, exp - 1)

    if n < 0:
        x = 1 / x
        n = -n

    return fast_pow(x, n)


# Iterative version:
def myPow_iterative(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2

    return result


# Test cases
if __name__ == "__main__":
    print(myPow(2.00000, 10))   # 1024.0
    print(myPow(2.10000, 3))    # 9.261
    print(myPow(2.00000, -2))   # 0.25
