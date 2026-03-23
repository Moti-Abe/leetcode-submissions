class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(x):
            mp = {}
            l, r, n = 0, 0, len(nums)
            count_subarray = 0
            if x == 0:
                return 0
            while r < n:
                mp[nums[r]] = mp.get(nums[r], 0) + 1

                while len(mp) > x:
                    mp[nums[l]] -= 1
                    if mp[nums[l]] == 0:
                        del mp[nums[l]]
                    l += 1

                count_subarray += (r - l + 1)

                r += 1
            
            return count_subarray
        
        ans =  helper(k) - helper(k-1)

        return ans
                
