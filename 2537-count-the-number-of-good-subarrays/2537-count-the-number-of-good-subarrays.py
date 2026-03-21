class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        equal_pairs = 0
        good_subarray = 0
        mp = {}
        left = 0

        for r in range(n):
            mp[nums[r]] = mp.get(nums[r], 0) + 1
            if mp[nums[r]] >= 2:
                equal_pairs += mp[nums[r]] - 1
            
            while equal_pairs >= k:
                good_subarray += (n - r)
                
                count = mp[nums[left]]
                equal_pairs -= (count - 1)
                mp[nums[left]] -= 1
                left += 1

        return good_subarray