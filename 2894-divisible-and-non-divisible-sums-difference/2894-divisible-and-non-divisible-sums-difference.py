class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1, sum2 = 0, 0
        for i in range(1, n+1):
            if i%m != 0:
                sum1 += i
            else:
                sum2 += i
        
        return sum1-sum2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna