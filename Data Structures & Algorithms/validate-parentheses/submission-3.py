class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inverse = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        
        for char in s:
            if char in inverse:
                stack.append(char)
            elif stack and inverse[stack[-1]] == char:
                stack.pop()
            else:
                return False
        
        return not stack
        