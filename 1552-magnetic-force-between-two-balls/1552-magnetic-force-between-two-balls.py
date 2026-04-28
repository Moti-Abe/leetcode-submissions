from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        
        def can_place(d):
            count = 1  # first ball at position[0]
            last = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last >= d:
                    count += 1
                    last = position[i]
                
                if count >= m:
                    return True
            
            return False
        
        low, high = 1, position[-1] - position[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_place(mid):
                ans = mid
                low = mid + 1   # try bigger distance
            else:
                high = mid - 1  # reduce distance
        
        return ans