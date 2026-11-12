class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        res = []
        for num in nums:
            if num < pivot:
                res.append(num)
        for num in nums:
            if num == pivot:
                res.append(num)
        for num in nums:
            if num > pivot:
                res.append(num)
        
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna