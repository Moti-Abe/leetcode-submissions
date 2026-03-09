class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        output = nums[0] + nums[1] + nums[n-1]
        min_dif = abs(output - target)

        for i in range (n-2):
            left, right  = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                dif = abs(target - total)
                if dif < min_dif:
                    min_dif = dif
                    output = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return output



        