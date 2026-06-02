from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2:
            return False

        s1_len = len(s1)
        s2_len = len(s2)

        s1_counter = Counter(s1)

        if s2_len < s1_len:
            return False

        l = 0
        r = s1_len

        s2_substring_counter = Counter(s2[l:r])

        while r <= s2_len:
            if s1_counter == s2_substring_counter:
                return True
            
            s2_substring_counter[s2[l]] -= 1
            l += 1

            if r < s2_len:
                s2_substring_counter[s2[r]] += 1

            r += 1
        
        return False
        