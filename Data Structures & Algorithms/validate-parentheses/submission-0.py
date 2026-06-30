class Solution:
    def isValid(self, s: str) -> bool:

        matches = {
            ')' : '(',
            ']': '[',
            '}': '{'
        }

        stack = []


        for char in s:
            if char in matches:
                if not stack or stack[-1] != matches[char]:
                    
                    return False
                else:
                    stack.pop()
                   
            
            else:
                stack.append(char)
        return True if len(stack) == 0 else False
        