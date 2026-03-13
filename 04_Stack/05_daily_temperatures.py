"""
Problem: Daily Temperatures (LeetCode #739)
Difficulty: Medium

CLARIFYING QUESTIONS:
- If no warmer day exists for a day, result is 0? (Yes)
- Temperatures are always positive integers? (Yes)
- Can all temperatures be the same? (Yes, result is all zeros)

APPROACH / PSEUDOCODE:
- Use a monotonic decreasing stack storing indices
- For each day i:
    - While stack non-empty and temperatures[i] > temperatures[stack top]:
        - Pop index j from stack
        - result[j] = i - j (days waited)
    - Push i to stack
- Remaining indices in stack never found warmer day → result stays 0

Time Complexity: O(n) - each index pushed/popped at most once
Space Complexity: O(n) - stack
"""

from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []  # monotonic decreasing stack of indices

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)

    return result


# Test cases
if __name__ == "__main__":
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
    print(dailyTemperatures([30,40,50,60]))               # [1,1,1,0]
    print(dailyTemperatures([30,60,90]))                  # [1,1,0]
