class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = []
        negative = []
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
        
        l, r = 0, 0
        
        res = []
        while positive and negative and l < len(positive) and r < len(negative):
            res.append(positive[l])
            res.append(negative[r])
            l += 1
            r += 1
        
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna