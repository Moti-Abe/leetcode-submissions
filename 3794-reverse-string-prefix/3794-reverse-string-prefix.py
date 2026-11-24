class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        l, r = 0, k-1
        s = list(s)
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna