class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)
        for i in range(n):
            map[nums[i]] = i
        
        for index,num in enumerate(nums):
            if target - num in map and index != map[target - num]:
                return [index, map[target - num]]



        