class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        majority_element = 0
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        
        for key, value in mp.items():
            if value > len(nums)/2:
                majority_element = key

        return majority_element 


        