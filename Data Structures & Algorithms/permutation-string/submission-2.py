class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2:
            return False

        s1_len = len(s1)
        s2_len = len(s2)

        s1_sorted = ''.join(sorted(s1))

        if s2_len < s1_len:
            return False

        l = 0
        r = s1_len

        while r <= s2_len:
            if s1_sorted == ''.join(sorted(s2[l:r])):
                return True
            
            l += 1
            r += 1
        
        return False
        