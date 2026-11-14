class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            if num%3 == 0:
                continue
            total += 1
        
        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna