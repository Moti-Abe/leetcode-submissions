class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st = deque()
        output = []
        for i in range(len(nums)):
            while st and st[0][0] <= i-k:
                st.popleft()
                
            while st and st[-1][1] < nums[i]: 
                st.pop()
            
            st.append((i, nums[i]))
            
            if st and i >= k-1:
                output.append(st[0][1])
        
        return output

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna