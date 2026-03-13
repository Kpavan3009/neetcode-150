"""
Problem: Search a 2D Matrix (LeetCode #74)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Each row is sorted, and first element of each row > last element of previous row? (Yes)
- Can the matrix be empty? (No, guaranteed m x n with m,n >= 1)
- Return True/False? (Yes)

APPROACH / PSEUDOCODE:
- Treat the 2D matrix as a flattened sorted array
- Binary search on virtual indices 0 to m*n-1
- To map virtual index mid to matrix: row = mid // n, col = mid % n
- Standard binary search from there

Time Complexity: O(log(m*n)) = O(log m + log n)
Space Complexity: O(1)
"""

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        val = matrix[mid // n][mid % n]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test cases
if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(searchMatrix(matrix, 3))   # True
    print(searchMatrix(matrix, 13))  # False
