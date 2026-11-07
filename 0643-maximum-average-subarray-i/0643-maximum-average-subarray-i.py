class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        widow_sum = sum(nums[0:k])
        max_sum = widow_sum
        left = 0
        for right in range (k,len(nums)):
            widow_sum += nums[right]
            widow_sum -= nums[left]

            max_sum = max(max_sum,widow_sum)
            left += 1
        
        return max_sum/k


        