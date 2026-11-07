class Solution:
    def arrangeCoins(self, n: int) -> int:
        complete_rows = 0

        while n > 0:
            complete_rows += 1
            n -= complete_rows
        
        if n < 0:
            return complete_rows-1
        else:
            return complete_rows