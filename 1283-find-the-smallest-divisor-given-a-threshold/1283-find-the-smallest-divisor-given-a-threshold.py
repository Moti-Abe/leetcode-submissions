class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def div_sum(nums, res):
            total_sum = 0.0
            for i in range (len(nums)):
                total_sum += math.ceil(nums[i]/res)
            return total_sum
        
        low, high = 1, max(nums)
        smallest_divisor = max(nums)
        while low <= high:
            mid = (low+high)//2
            res_sum = div_sum(nums,mid)
            if res_sum <= threshold:
                smallest_divisor = min(smallest_divisor, mid)
                high = mid-1
            else:
                low = mid+1

        return smallest_divisor