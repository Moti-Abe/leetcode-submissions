class MinStack:

    def __init__(self):
        self.stack = deque()
        self.val = 0

    def push(self, val: int) -> None:
        self.val = val
        if not self.stack:
            self.stack.append((self.val, self.val))
        else:
            x = self.stack[-1][1]
            if self.val <= x:
                self.stack.append((self.val, self.val))
            else:
                self.stack.append((self.val, x))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()