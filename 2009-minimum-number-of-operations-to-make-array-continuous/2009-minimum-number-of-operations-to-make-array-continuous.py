from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))  # remove duplicates
        
        max_window = 0
        j = 0
        
        for i in range(len(nums)):
            while j < len(nums) and nums[j] < nums[i] + n:
                j += 1
            
            max_window = max(max_window, j - i)
        
        return n - max_window