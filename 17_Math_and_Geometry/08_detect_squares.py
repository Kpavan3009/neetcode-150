"""
Problem: Detect Squares (LeetCode #2013)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Axis-aligned squares only? (Yes)
- Can points be added multiple times? (Yes, count matters for count())
- count() returns number of ways to form squares? (Yes)

APPROACH / PSEUDOCODE:
- Store points with their counts in a hash map
- For count(point): fix two diagonal points of the square
    - For each existing point (px, py):
        - The query point (qx, qy) and (px, py) can be diagonals if they form a square
        - Need: side = |px - qx| == |py - qy| (and side > 0)
        - Two other corners: (qx, py) and (px, qy)
        - Count = pts[px][py] * pts[qx][py] * pts[px][qy]

Time Complexity: add O(1), count O(n) where n = unique x values * unique y values
Space Complexity: O(n)
"""

from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.pt_counts = defaultdict(int)  # (x, y) -> count
        self.x_set = defaultdict(set)      # x -> set of y values

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pt_counts[(x, y)] += 1
        self.x_set[x].add(y)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total = 0

        # Fix diagonal: (px, py) where px != qx, forming a square
        for py in self.x_set[qx]:
            if py == qy:
                continue
            side = abs(py - qy)
            # Two possible squares: x = qx + side, qx - side
            for px in [qx + side, qx - side]:
                total += (self.pt_counts[(qx, py)] *
                          self.pt_counts[(px, qy)] *
                          self.pt_counts[(px, py)])

        return total


# Test cases
if __name__ == "__main__":
    ds = DetectSquares()
    ds.add([3,10])
    ds.add([11,2])
    ds.add([3,2])
    print(ds.count([11,10]))  # 1
    print(ds.count([14,8]))   # 0
    ds.add([11,2])
    print(ds.count([11,10]))  # 2
