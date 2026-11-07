class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        mx_right = nums[-1]
        max_right = [0]*n
        for i in range(n-1,-1,-1):
            mx_right = max(mx_right, nums[i])
            max_right[i] = mx_right
        
        l, r = 0, 0
        ans = 0
        while r < n and l < n:
            if nums[l] <= max_right[r]:
                ans = max(ans,r-l)
                r += 1
            else:
                l += 1 
            
        return ans




