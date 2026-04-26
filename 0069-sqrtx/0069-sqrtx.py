class Solution:
    def mySqrt(self, x: int) -> int:
        n = 50000
        arr = []
        for i in range (n):
            arr.append(i**2)
        
        low, high = 0, n-1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] < x:
                low = mid+1
            elif arr[mid] > x:
                high = mid-1
            else:
                return mid
        return high
        