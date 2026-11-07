from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sum = 0
        for i in range(len(tickets)):
            if tickets[i] >= tickets[k]:
                if i <= k:
                    sum += tickets[k]
                else:
                    sum += tickets[k] - 1
            else:
                sum += tickets[i]
        
        return sum