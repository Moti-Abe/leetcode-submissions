class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            res.append(num)
        for i in range(len(nums)-1,-1,-1):
            res.append(nums[i])
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna