class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set()
        for num in nums:
            st.add(num)
        if(len(st) == len(nums)):
            return False
        else:
            return True


        