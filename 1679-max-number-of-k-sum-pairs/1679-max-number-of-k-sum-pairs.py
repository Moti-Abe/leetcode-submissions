class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        output = 0
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            sum_of_two = nums[left] + nums[right]
            if sum_of_two < k:
                left += 1
            elif sum_of_two > k:
                right -= 1
            else:
                output += 1
                left += 1
                right -= 1
        return output


