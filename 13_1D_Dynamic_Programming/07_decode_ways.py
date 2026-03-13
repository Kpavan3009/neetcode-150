"""
Problem: Decode Ways (LeetCode #91)
Difficulty: Medium

CLARIFYING QUESTIONS:
- '0' alone is invalid; "10" and "20" are valid (as 10, 20)? (Yes)
- String with leading '0' has 0 ways? (Yes)
- Letters map: 'A'=1, ..., 'Z'=26 (only 1-26 are valid)? (Yes)

APPROACH / PSEUDOCODE:
- dp[i] = number of ways to decode s[0..i-1]
- dp[0] = 1 (empty string), dp[1] = 1 if s[0] != '0' else 0
- For each position i:
    - One-digit decode: if s[i-1] != '0' → dp[i] += dp[i-1]
    - Two-digit decode: if s[i-2:i] is between 10-26 → dp[i] += dp[i-2]
- Space optimize to O(1)

Time Complexity: O(n)
Space Complexity: O(1)
"""


def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    prev2, prev1 = 1, 1  # dp[i-2], dp[i-1]

    for i in range(2, len(s) + 1):
        curr = 0
        # One-digit decode
        if s[i-1] != '0':
            curr += prev1
        # Two-digit decode
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            curr += prev2
        prev2 = prev1
        prev1 = curr

    return prev1


# Test cases
if __name__ == "__main__":
    print(numDecodings("12"))   # 2 ("AB" or "L")
    print(numDecodings("226"))  # 3 ("BBF", "BZ", "VF")
    print(numDecodings("06"))   # 0
