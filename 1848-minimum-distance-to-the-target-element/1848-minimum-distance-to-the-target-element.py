class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_diff = 10000
        for i in range (len(nums)):
            if nums[i] == target:
                min_diff = min(min_diff, abs(i-start))

        return min_diff