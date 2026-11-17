class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        arr = deque()
        avg = []
        for num in nums:
            arr.append(num)

        while arr:
            avg.append((arr[0] + arr[-1])/2)
            arr.pop()
            arr.popleft()
            
        return min(avg)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna