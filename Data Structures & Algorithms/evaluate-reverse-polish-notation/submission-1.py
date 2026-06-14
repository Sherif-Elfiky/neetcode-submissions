class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        operators = ['+', '-', '*', '/']

        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(token)
                continue
            
            x = int(stack.pop())
            y = int(stack.pop())

            if token == '+':
                stack.append(x + y)
        

            elif token == '-':
                stack.append(y - x)
            
            elif token == '*':
                stack.append(x * y)
            else:
                stack.append(y / x)
        return int(stack[-1])




        