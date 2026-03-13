"""
Problem: Climbing Stairs (LeetCode #70)
Difficulty: Easy

CLARIFYING QUESTIONS:
- Can take 1 or 2 steps at a time? (Yes)
- n >= 1 always? (Yes)

APPROACH / PSEUDOCODE:
- dp[i] = number of ways to reach step i
- dp[1] = 1, dp[2] = 2
- dp[i] = dp[i-1] + dp[i-2] (Fibonacci-like)
- Optimize to O(1) space using two variables

Time Complexity: O(n)
Space Complexity: O(1)
"""


def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    prev1, prev2 = 1, 2  # dp[i-2], dp[i-1]
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    return prev2


# Test cases
if __name__ == "__main__":
    print(climbStairs(2))  # 2
    print(climbStairs(3))  # 3
    print(climbStairs(5))  # 8
