class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        min_val = min(x, y//4)
        
        if min_val%2 == 0:
            return "Bob"
        else:
            return "Alice" 