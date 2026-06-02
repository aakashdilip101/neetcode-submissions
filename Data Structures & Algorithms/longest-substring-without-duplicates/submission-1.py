class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_set = set(s[0])
        l = 0
        r = 1
        substring_len = 1 

        while (r < len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            if len(char_set) > substring_len:
                substring_len = len(char_set)
            
            r += 1
        
        return substring_len