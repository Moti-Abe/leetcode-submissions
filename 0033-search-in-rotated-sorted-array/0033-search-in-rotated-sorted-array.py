class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target <= nums[r] and target >= nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
        return -1



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna