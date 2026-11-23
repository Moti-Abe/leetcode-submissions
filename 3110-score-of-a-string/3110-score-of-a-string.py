class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            res += abs(ord(s[i]) - ord(s[i+1]))
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna