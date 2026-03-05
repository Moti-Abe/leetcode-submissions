class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        count = 0
        output = []
        nums.sort()
        for i in range (len(nums)-1):
            if nums[i+1] > nums[i]:
                count += 1
                output.append(count)
            else:
                output.append(count)
        
        return sum(output)
            


        
        return output
            



        