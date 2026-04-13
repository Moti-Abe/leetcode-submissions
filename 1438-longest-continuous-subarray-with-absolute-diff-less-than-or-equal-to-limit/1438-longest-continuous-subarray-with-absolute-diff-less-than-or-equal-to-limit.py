from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_d = deque()
        min_d = deque()
        res = 0
        l = 0

        for r in range (len(nums)):
            while max_d and nums[r] > max_d[-1]:
                max_d.pop()
            max_d.append(nums[r])

            while min_d and nums[r] < min_d[-1]:
                min_d.pop()
            min_d.append(nums[r])

            while max_d[0] - min_d[0] > limit:
                if nums[l] == max_d[0]:
                    max_d.popleft()
                if nums[l] == min_d[0]:
                    min_d.popleft()
                l += 1
            res = max(res, r-l+1)
        
        return res
