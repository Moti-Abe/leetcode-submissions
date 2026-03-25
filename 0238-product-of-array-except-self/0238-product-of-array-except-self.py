class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1

        for i in range(len(nums)):
            if nums[i] != 0:
                total_product *= nums[i]

        zeros = nums.count(0)
        if zeros == 0:
            for i in range(len(nums)):
                nums[i] = total_product//nums[i]
        elif zeros > 1:
            return [0]*len(nums)
        elif zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = total_product
                else:
                    nums[i] = 0
        
        return nums