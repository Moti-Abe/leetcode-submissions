class StockSpanner:

    def __init__(self):
        self.stack = deque()
        self.i = -1
        
    def next(self, price: int) -> int:
        self.i += 1
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()

        if self.stack:
            span = self.i - self.stack[-1][0]
        else:
            span = self.i + 1
             
        self.stack.append((self.i,price))
    
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)