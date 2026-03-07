class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        left , right = m-1 , n-1
        res_len = len(nums1) - 1

        while left > -1 and right > -1:
            if nums1[left] <= nums2[right]:
                nums1[res_len] = nums2[right]
                res_len -= 1
                right -= 1
            else:
                nums1[res_len] = nums1[left]
                res_len -= 1
                left -= 1 
                
        while left == -1 and right > -1:
            nums1[res_len] = nums2[right]
            right -= 1
            res_len -= 1
        

        