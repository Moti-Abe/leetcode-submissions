class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i

        
        for i in range(len(nums)):
            num = target - nums[i]
            if num in mp and i != mp[num]:
                return [i,mp[num]]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna