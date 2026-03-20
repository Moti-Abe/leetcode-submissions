class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        total = 0
        n = len(nums)
        output = [-1] * n
        
        if n%2 == 1 and k > (n//2):
            return output
        if n%2 == 0 and k > ((n//2) - 1):
            return output
            
        left, right = 0, 2*k + 1
        ind = k
        for i in range (2*k+1):
            total += nums[i]
        
        while right <= n:
            output[ind] = total//(2*k + 1)
            ind += 1
            if right == n:
                break
            total -= nums[left]
            left += 1
            total += nums[right]
            right += 1
        
        return output


        

        
    