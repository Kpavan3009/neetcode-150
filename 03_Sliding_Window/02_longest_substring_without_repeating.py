"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Difficulty: Medium

CLARIFYING QUESTIONS:
- Can the string be empty? (Yes, return 0)
- Only ASCII characters or Unicode? (Assume all printable ASCII)
- Are spaces considered characters? (Yes)

APPROACH / PSEUDOCODE:
- Sliding window with a hash map storing character → last seen index
- Expand right pointer, adding characters to window
- If a character is repeated and within current window:
    - Jump left pointer to just after the previous occurrence
- Track maximum window size at each step

Time Complexity: O(n) - each character visited at most twice
Space Complexity: O(min(n, m)) where m = charset size (at most 128 for ASCII)
"""


def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}  # char -> most recent index
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1

        char_index[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# Test cases
if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
    print(lengthOfLongestSubstring("bbbbb"))     # 1 ("b")
    print(lengthOfLongestSubstring("pwwkew"))    # 3 ("wke")
    print(lengthOfLongestSubstring(""))          # 0
