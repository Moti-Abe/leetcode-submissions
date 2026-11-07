class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        output = []
        for i in range(len(order)):
            if order[i] in friends:
                output.append(order[i])
        
        return output

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna