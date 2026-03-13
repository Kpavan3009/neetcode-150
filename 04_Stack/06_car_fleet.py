"""
Problem: Car Fleet (LeetCode #853)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Cars at the same position form a fleet from the start? (Yes)
- What if a faster car catches a slower car? (They form a fleet, travel at slower speed)
- Are positions all distinct? (Yes, per problem constraints)
- What if no cars? (Return 0)

APPROACH / PSEUDOCODE:
- Pair each car's (position, speed) and sort by position descending (closest to target first)
- Compute time to reach target for each car: time = (target - pos) / speed
- Use a stack:
    - For each car's time (sorted by position descending):
        - If stack non-empty and current time <= stack top → same fleet (car catches up)
        - Else → new fleet, push time to stack
- Stack size = number of fleets

Time Complexity: O(n log n) - sorting
Space Complexity: O(n) - stack
"""

from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)  # sort by position descending
    stack = []  # stores time to reach target for each fleet leader

    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
        # else: this car catches the fleet ahead → same fleet, don't push

    return len(stack)


# Test cases
if __name__ == "__main__":
    print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))  # 3
    print(carFleet(10, [3], [3]))                     # 1
    print(carFleet(100, [0,2,4], [4,2,1]))            # 1
