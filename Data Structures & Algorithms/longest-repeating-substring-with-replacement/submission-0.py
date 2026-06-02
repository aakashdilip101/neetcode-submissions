from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        l = 0
        r = 0
        largest_window = 0

        while r < len(s):
            char_counts = Counter(s[l:(r + 1)])
            most_freq = max(char_counts.values())
            if ((r + 1) - l - most_freq) > k:
                l += 1
            else:
                largest_window = max(((r + 1) - l), largest_window)
                r += 1
        
        return largest_window