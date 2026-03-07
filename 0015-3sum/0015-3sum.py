class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []
        for i in range (len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    output.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        output = list(set(output))
        return output



