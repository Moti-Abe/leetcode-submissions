class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ind, k = 0, 0
        n = len(arr)
        max_len = 0
        while k < n-1:
            if k%2 == 0:
                if arr[k] < arr[k+1]:
                    k += 1
                else:
                    k += 1
                    ind = k
            else:
                if arr[k] > arr[k+1]:
                    k += 1
                else:
                    k += 1
                    ind = k
            max_len = max(max_len, k-ind+1)
        
        ind, k = 0, 0
        while k < n-1:
            if k%2 == 1:
                if arr[k] < arr[k+1]:
                    k += 1
                else:
                    k += 1
                    ind = k
            else:
                if arr[k] > arr[k+1]:
                    k += 1
                else:
                    k += 1
                    ind = k
            max_len = max(max_len, k-ind+1)
        
        if len(arr) == 1:
            return 1
        else:
            return max_len
     