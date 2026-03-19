class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = []
        for i in range (len(nums)):
            start = max(0, i - nums[i])
            total_sum = 0
            for j in range(start, i+1):
                total_sum += nums[j] 
            res.append(total_sum)
        return sum(res)
        