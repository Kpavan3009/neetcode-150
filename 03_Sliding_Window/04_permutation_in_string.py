"""
Problem: Permutation in String (LeetCode #567)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Is it asking if any permutation of s1 is a substring of s2? (Yes)
- Only lowercase letters? (Yes)
- Can s1 be longer than s2? (Yes, return False)

APPROACH / PSEUDOCODE:
- Fixed-size sliding window of length len(s1) over s2
- Use character frequency counts: need[char] = count in s1
- Track how many chars have matched their required frequency (matches counter)
- Slide window: add right char, remove left char, update matches
- If matches == 26 → found a valid permutation window

Time Complexity: O(n) where n = len(s2)
Space Complexity: O(1) - arrays of size 26
"""


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    need = [0] * 26
    window = [0] * 26

    for ch in s1:
        need[ord(ch) - ord('a')] += 1

    k = len(s1)
    matches = 0

    # Initialize window with first k characters
    for i in range(k):
        idx = ord(s2[i]) - ord('a')
        window[idx] += 1

    for i in range(26):
        if window[i] == need[i]:
            matches += 1

    if matches == 26:
        return True

    for right in range(k, len(s2)):
        # Add new character on right
        r_idx = ord(s2[right]) - ord('a')
        window[r_idx] += 1
        if window[r_idx] == need[r_idx]:
            matches += 1
        elif window[r_idx] == need[r_idx] + 1:
            matches -= 1

        # Remove character on left
        l_idx = ord(s2[right - k]) - ord('a')
        window[l_idx] -= 1
        if window[l_idx] == need[l_idx]:
            matches += 1
        elif window[l_idx] == need[l_idx] - 1:
            matches -= 1

        if matches == 26:
            return True

    return False


# Test cases
if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))  # True  ("ba" is permutation of "ab")
    print(checkInclusion("ab", "eidboaoo"))  # False
