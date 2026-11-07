class Solution:
    def countTriples(self, n: int) -> int:
        output = 0
        nums = [num for num in range(1,n+1)]
        for i in range(n):
            for j in range(n):
                if math.sqrt(nums[i]**2 + nums[j]**2) in nums:
                    output += 1
        
        return output



        