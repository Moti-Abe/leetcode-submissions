class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        n = len(nums)
        nge = [-1]*n

        for i in range (2*n-1,-1,-1):
            ind = i%n
            while stack and stack[-1] <= nums[ind]:
                stack.pop()
            if i < n:
                if stack:
                    nge[i] = stack[-1]
        
            stack.append(nums[ind])
           
        return nge