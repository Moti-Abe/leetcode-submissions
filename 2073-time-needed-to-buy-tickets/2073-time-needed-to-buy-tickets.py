from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()

        for i in range(len(tickets)):
            q.append((i,tickets[i]))
        
        time = 0
        while True:
            i, t = q.popleft()
            t -= 1
            
            time += 1

            if i == k and t == 0:
                return time
            
            if t > 0:
                q.append((i,t))