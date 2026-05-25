class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        
        prefix[0] = nums[0]
        for i in range(1,n):
            num = nums[i]
            if num == 0:
                num = 1
            prefix[i] = prefix[i-1]*num
        
        zeros = nums.count(0)
        if zeros > 1:
            return [0]*n
        elif zeros == 1:
            ind = nums.index(0)
            nums.remove(0)
            res = [0]*n
            res[ind] = math.prod(nums)
            return res
        
        for i in range(n):
            prefix[i] = prefix[-1]//nums[i]
        
        return (prefix)


