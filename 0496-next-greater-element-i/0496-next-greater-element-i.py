class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        mp = {}
        for i in range(len(nums2)):
            mp[nums2[i]] = i
        
        for i in range(len(nums1)):
            for j in range (mp[nums1[i]], len(nums2)):
                if nums1[i] < nums2[j]:
                    output.append(nums2[j])
                    break
            else:
                output.append(-1)
        
        return output
