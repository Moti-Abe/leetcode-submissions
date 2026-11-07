class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def helper(x):
            left, right, total, count = 0, 0, 0, 0
            while right < len(nums):
                if nums[right]%2 == 0:
                    total += 0
                else:
                    total += 1
                
                while total > x:
                    if nums[left]%2 == 1:
                        total -= 1
                    left += 1
                
                count += (right - left + 1)
                right += 1

            return count
        
        return helper(k) - helper(k-1)

