class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        nearst_nums = []

        for i in range(n):
           nearst_nums.append([abs(x-arr[i]), arr[i]])
        
        nearst_nums.sort()

        output = []
        for i in range(k):
            output.append(nearst_nums[i][1])
        
        return sorted(output)

