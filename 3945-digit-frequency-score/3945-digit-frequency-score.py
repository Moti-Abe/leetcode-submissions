class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        mp = {}
        n = str(n)
        for i in range(len(n)):
            mp[n[i]] = mp.get(n[i], 0) + 1

        output = 0
        for key, val in mp.items():
            output += (int(key) * val)
        
        return output

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna