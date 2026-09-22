class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in range (len(tokens)):
            if tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/':
                x = stack.pop()
                y = stack.pop()
                if tokens[i] != '/':
                    res = eval(f"{y} {tokens[i]} {x}")
                else:
                    res = int(y/x)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]
