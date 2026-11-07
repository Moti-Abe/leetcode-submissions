class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)- 1
        while l < r:
            while r >= 0 and nums[r] == val:
                r -= 1
            while l < len(nums) and nums[l] != val:
                l += 1
            if l >= r:
                break
            if l < len(nums) and r > -1:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        
        return len(nums)-nums.count(val)