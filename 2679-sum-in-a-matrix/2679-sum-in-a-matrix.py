class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows , cols = len(nums), len(nums[0])

        output = 0
        for i in range (cols):
            max_num = 0
            for j in range (rows):
                num = max(nums[j])
                nums[j].remove(num)
                max_num = max(max_num,num)
            output += max_num
        return output


        