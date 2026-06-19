class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        operator_map = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)  
        }

        for token in tokens:
            if token in operator_map:
                num2 = stack.pop()
                num1 = stack.pop()
                
                result = operator_map[token](num1, num2)
                stack.append(result)
            else:
                stack.append(int(token))
                
        return stack[0]



        