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
                    res = f"{y} {tokens[i]} {x}"
                    st.append(int(eval(res))) 
        return int(st[0])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna