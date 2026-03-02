class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        output = 0
        for i in range (len(arr)-2):
            for j in range (i+1,len(arr)-1):
                for k in range(j+1,len(arr)):

                    x = abs(arr[i] - arr[j]) 
                    y = abs(arr[j] - arr[k])
                    z = abs(arr[i] - arr[k])
                    if x <= a and y <= b and z <= c:
                        output += 1
                        
        return output


        