class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subset = []
        for r in range(len(nums)+1):
            for subset in combinations(nums, r):
                all_subset.append(subset)
        
        return all_subset

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna