"""
Problem: Minimum Window Substring (LeetCode #76)
Difficulty: Hard

CLARIFYING QUESTIONS:
- If no valid window exists, return empty string? (Yes)
- Can t have duplicate characters? (Yes, window must contain all occurrences)
- Can s or t be empty? (t is non-empty; if s is empty return "")
- Is the answer guaranteed to be unique? (Yes, but if no answer return "")

APPROACH / PSEUDOCODE:
- Use sliding window with two frequency maps: need (target) and have (window)
- Track 'formed': number of unique chars in window meeting required frequency
- Expand right; when all chars satisfied → try to shrink from left
- Record minimum window whenever all chars are satisfied

Time Complexity: O(|s| + |t|)
Space Complexity: O(|s| + |t|)
"""

from collections import Counter


def minWindow(s: str, t: str) -> str:
    if not t:
        return ""

    need = Counter(t)
    window = {}
    required = len(need)  # unique chars we need to satisfy
    formed = 0            # unique chars currently satisfied

    left = 0
    min_len = float('inf')
    min_start = 0

    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        if ch in need and window[ch] == need[ch]:
            formed += 1

        while formed == required:
            # Update answer
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_start = left

            # Shrink from left
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

    return s[min_start: min_start + min_len] if min_len != float('inf') else ""


# Test cases
if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
    print(minWindow("a", "a"))                # "a"
    print(minWindow("a", "aa"))               # ""
