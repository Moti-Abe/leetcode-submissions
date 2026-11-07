class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        mp = {0:-1}
        for i in range(len(nums)):
            rem = nums[i]%k
            if rem in mp:
                if i - mp[rem] > 1:
                    return True
            else:
                mp[rem] = i
        
        return False
            
