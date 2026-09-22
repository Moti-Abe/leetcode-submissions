class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = deque()
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                st.append(int(tokens[i]))
            else:
                if len(st) >= 2:
                    x = st.pop()
                    y = st.pop()
                    if tokens[i] == "+":
                        res = y + x
                    elif tokens[i] == "-":
                        res = y - x
                    elif tokens[i] == "*":
                        res = y * x
                    else:
                        res = int(y / x)
                    st.append(res) 
        return st[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna