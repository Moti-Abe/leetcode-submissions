class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                # build substring
                temp = []
                while stack and stack[-1] != '[':
                    temp.append(stack.pop())
                temp.reverse()  # correct order

                stack.pop()  # remove '['

                # get number (can be multiple digits)
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num.reverse()
                num = int("".join(num))
                
                # repeat and push back
                decoded = "".join(temp) * num
                for ch in decoded:
                    stack.append(ch)

        return "".join(stack)