class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp, freq = {}, [[] for i in range(len(nums)+1)]
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        output = []
        for key, value in mp.items():
            freq[value].append(key)
        
        output = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna