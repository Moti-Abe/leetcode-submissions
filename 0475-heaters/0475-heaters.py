from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        radius = 0
        
        for house in houses:
            # Find insertion position in heaters
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to the nearest heater on the left
            left_dist = float('inf')
            if idx > 0:
                left_dist = house - heaters[idx - 1]
            
            # Distance to the nearest heater on the right
            right_dist = float('inf')
            if idx < len(heaters):
                right_dist = heaters[idx] - house
            
            # Closest heater distance for this house
            min_dist = min(left_dist, right_dist)
            
            # Update global radius (worst-case house)
            radius = max(radius, min_dist)
        
        return radius