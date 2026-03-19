class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mp = {}
        l = 0
        n = len(nums)
        max_sum = 0
        window_sum = 0
        for r in range(n):
            mp[nums[r]] = mp.get(nums[r], 0) + 1
            window_sum += nums[r]
            
            while len(mp) < (r-l+1):
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0:
                    del mp[nums[l]]
                window_sum -= nums[l]
                l += 1
            max_sum = max(max_sum, window_sum)
            r += 1
        
        return max_sum
