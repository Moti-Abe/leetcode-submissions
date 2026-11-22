class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return output

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna