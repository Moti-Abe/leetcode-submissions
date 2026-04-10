class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = deque()
        nge = [0] * n
        mp = {}
        for i in range (n-1,-1,-1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]
            else:
                nge[i] = -1
            stack.append(nums2[i])
        
        for i in range (n):
            mp[nums2[i]] = nge[i]
        
        res = [0]*len(nums1)
        for i in range(len(nums1)):
            res[i] = mp[nums1[i]]
        
        return res

