class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        res = 1
        if n%2 == 0:
            res = pow(5,(n//2),mod)
            res *= pow(4, n//2, mod)
        else:
            res = pow(5,(n//2 + 1),mod)
            res *= pow(4, n//2, mod)
        
        return res% mod