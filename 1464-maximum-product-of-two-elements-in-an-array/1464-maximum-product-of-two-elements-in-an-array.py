class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        mx = max(nums)
        nums.remove(mx)
        mx2 = max(nums)
        
        nums.remove(mx2)


        return ((mx-1)*(mx2-1))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna