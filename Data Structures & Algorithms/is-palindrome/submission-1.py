class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s) - 1
        start = 0

        while start < end:
            c_start = s[start]
            c_end = s[end]
            
            if not c_start.isalnum():
                start += 1
            elif not c_end.isalnum():
                end -= 1
            elif c_start.lower() != c_end.lower():
                return False
            else:
                start += 1
                end -= 1
        
        return True
