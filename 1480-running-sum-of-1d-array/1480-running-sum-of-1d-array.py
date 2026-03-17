class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            output.append(total)
        return output