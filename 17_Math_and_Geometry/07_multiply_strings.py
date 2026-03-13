"""
Problem: Multiply Strings (LeetCode #43)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Inputs are non-negative integer strings? (Yes)
- Can't use built-in big integer multiplication? (Correct, implement from scratch)
- Can inputs be "0"? (Yes)

APPROACH / PSEUDOCODE:
- Grade-school multiplication:
    - Result has at most len(num1) + len(num2) digits
    - For each pair (i, j), multiply num1[i] * num2[j]
    - Add to positions [i+j] and [i+j+1] in result array
- Convert result array to string (handle leading zeros)

Time Complexity: O(m * n)
Space Complexity: O(m + n)
"""


def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            total = mul + result[p2]
            result[p2] = total % 10
            result[p1] += total // 10

    # Skip leading zeros
    result_str = ''.join(map(str, result)).lstrip('0')
    return result_str or "0"


# Test cases
if __name__ == "__main__":
    print(multiply("2", "3"))        # "6"
    print(multiply("123", "456"))    # "56088"
    print(multiply("9", "9"))        # "81"
