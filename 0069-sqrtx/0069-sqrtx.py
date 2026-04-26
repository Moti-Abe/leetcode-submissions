class Solution:
    def mySqrt(self, x: int) -> int:
        n = 50000
        arr = []
        for i in range (n):
            arr.append(i**2)
        
        for i in range (n):
            if arr[i] == x:
                return i
            elif arr[i] > x:
                return i-1