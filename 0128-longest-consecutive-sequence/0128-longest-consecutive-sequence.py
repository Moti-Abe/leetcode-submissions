class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        unique_nums = list(set(nums))
        unique_nums.sort()
        max_len = 1
        count = 1
        for i in range(1,len(unique_nums)):
            if unique_nums[i] - unique_nums[i-1] == 1:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 1
        return max_len
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna