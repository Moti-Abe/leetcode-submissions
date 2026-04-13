class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        nums.extend(nums)
        n = len(nums)
        nge = [-1]*n

        for i in range (n-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]
        
            stack.append(nums[i])
           
        return nge[:n//2]