class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = []
        for i in range(len(matrix)):
            res.append(sum(matrix[i]))
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna