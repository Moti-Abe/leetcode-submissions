class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        rev_alphabet = "abcdefghijklmnopqrstuvwxyz"
        rev_alphabet = rev_alphabet[::-1]
        mp = {}
        for i in range(26):
            mp[rev_alphabet[i]] = i+1
        for i in range(len(s)):
            total += (mp[s[i]] * (i+1))
        
        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna