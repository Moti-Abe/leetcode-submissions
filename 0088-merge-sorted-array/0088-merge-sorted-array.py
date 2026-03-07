class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        left , right = 0 , 0

        while left < m and right < n:
            if nums1[left] < nums2[right]:
                res.append(nums1[left])
                left += 1
            else:
                res.append(nums2[right])
                right += 1
        
        while left == m and right < n:
            res.append(nums2[right])
            right += 1
        
        while left < m and right == n:
            res.append(nums1[left])
            left += 1
        
        for i in range (len(res)):
            nums1[i] = res[i]

        