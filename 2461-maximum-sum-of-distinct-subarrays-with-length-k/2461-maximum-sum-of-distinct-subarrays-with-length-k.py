class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        left, right, window_sum = 0, k-1, 0

        for i in range (k):
            mp[nums[i]] = mp.get(nums[i], 0) + 1
            window_sum += nums[i] 
        
        max_sum = 0
        while right < len(nums):
            if len(mp) ==  (right - left + 1):
                max_sum  = max(max_sum, window_sum)
            
            mp[nums[left]] -= 1
            if mp[nums[left]] == 0:
                del mp[nums[left]]
            window_sum -= nums[left]
            left += 1
            right += 1
            
            if right == len(nums):
                break
            mp[nums[right]] = mp.get(nums[right], 0) + 1
            window_sum += nums[right]
            

        return max_sum