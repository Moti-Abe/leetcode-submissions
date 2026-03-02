class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        min_sum = 100000
        triplet_found = False
        for i in range (n-2):
            for j in range (i+1,n-1):
                if nums[i] >= nums[j]:
                    continue
                for k in range (j+1,n):
                    if nums[k] < nums[j]:
                        triplet_found = True
                        triplet_sum = nums[i] + nums[j] + nums[k]
                        min_sum = min(min_sum, triplet_sum)
        
        if triplet_found:
            return min_sum
        else:
            return -1


        