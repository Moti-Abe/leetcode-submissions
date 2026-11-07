class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = deque()
        for i in range (len(logs)):
            if stack and logs[i] == '../':
                stack.pop()
            elif logs[i] == './':
                continue
            elif logs[i] != '../' and logs[i] != './':
                stack.append(logs[i])
        
        return len(stack)