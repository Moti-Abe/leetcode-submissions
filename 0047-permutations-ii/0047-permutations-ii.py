class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        all_p = list(itertools.permutations(nums))
        all_p = set(all_p)

        return list(all_p)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna