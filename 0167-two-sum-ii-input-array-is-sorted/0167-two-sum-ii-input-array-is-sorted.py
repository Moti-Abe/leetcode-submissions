class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        left , right = 0, len(numbers)-1
        for i in range (len(numbers)):
            mp[numbers[i]] = i
        numbers.sort()

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return[left+1, right+1]

        

        