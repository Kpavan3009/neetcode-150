"""
Problem: Longest Repeating Character Replacement (LeetCode #424)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Only uppercase English letters? (Yes)
- Can k be 0? (Yes, no replacements allowed)
- Can k be larger than string length? (Yes, then answer is len(s))

APPROACH / PSEUDOCODE:
- Sliding window: maintain a window [left, right]
- Track frequency of each char in window using a count array
- Key insight: window is valid if (window_size - max_freq) <= k
  (we only need to replace non-dominant characters)
- Expand right; if window becomes invalid, shrink from left
- Track max window size seen

Time Complexity: O(n) - each element processed at most twice
Space Complexity: O(1) - count array of size 26
"""


def characterReplacement(s: str, k: int) -> int:
    count = {}
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
        ch = s[right]
        count[ch] = count.get(ch, 0) + 1
        max_freq = max(max_freq, count[ch])

        # Window size - max frequency = chars we need to replace
        window_size = right - left + 1
        if window_size - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# Test cases
if __name__ == "__main__":
    print(characterReplacement("ABAB", 2))   # 4
    print(characterReplacement("AABABBA", 1))  # 4
