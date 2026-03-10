class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        for i in range (k):
            total += nums[i]
        
        left , right = 0, k-1
        max_sum = total
        while right < len(nums)-1:
            total -= nums[left]
            left += 1
            right += 1
            total += nums[right]

            max_sum = max(max_sum, total)
        
        return max_sum/k


        