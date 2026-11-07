class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        output = []
        for num in nums:
            mp[num] = mp.get(num , 0) + 1
        
        for key, value in mp.items():
            if value > len(nums)/3:
                output.append(key)

        return output



        