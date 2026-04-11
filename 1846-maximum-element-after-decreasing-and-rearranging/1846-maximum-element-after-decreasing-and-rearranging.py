class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        count = 0
        arr.sort()
        arr[0] = 1
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) > 1:
                arr[i] = arr[i-1] + 1
                count += 1 
        
        return max(arr)