class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def subarraysLessGoal(g):
            if g < 0:
                return 0

            left, right, count, total = 0, 0, 0, 0

            while right < len(nums):
                total += nums[right]

                while total > g:
                    total -= nums[left]
                    left += 1
                count += (right - left + 1)
                right += 1

            return count
            
        return subarraysLessGoal(goal) - subarraysLessGoal(goal-1)