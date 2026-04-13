from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sl = SortedList()
        l = 0
        max_len = 0
        
        for r in range(len(nums)):
            sl.add(nums[r])
            
            while sl[-1] - sl[0] > limit:
                sl.remove(nums[l])
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len