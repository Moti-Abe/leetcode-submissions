class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0
        l, r = 0, len(height)-1
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = h*w

            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna