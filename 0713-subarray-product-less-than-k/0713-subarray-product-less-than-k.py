class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)

        l = 0
        count = 0

        for r in range(1, len(prefix)):
            while l < r and prefix[r] >= k * prefix[l]:
                l += 1

            count += (r - l)

        return count