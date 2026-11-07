class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mp = {}
        max_consecutive = 0
        for num in nums:
            mp[num] = mp.get(num,0) + 1
            if num == 1:
                max_consecutive = max(max_consecutive, mp[num])
            else:
                mp.clear()
        
        return max_consecutive
