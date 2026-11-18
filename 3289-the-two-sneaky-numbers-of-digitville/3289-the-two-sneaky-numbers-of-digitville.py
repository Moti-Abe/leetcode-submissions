class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        output = []
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
            if mp[num] > 1:
                output.append(num)
        
        output.sort()
        return output

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna