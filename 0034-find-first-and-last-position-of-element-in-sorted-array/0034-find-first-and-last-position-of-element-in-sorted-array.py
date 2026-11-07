class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1,-1
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid + 1
            else:
                start = mid
                r = mid-1

        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid + 1
            else:
                end = mid
                l = mid+1
        
        return [start,end]

