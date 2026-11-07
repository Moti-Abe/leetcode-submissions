from typing import List
from collections import Counter

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        
        # For each point as pivot
        for x1, y1 in points:
            dist_count = Counter()
            
            # Count distances from pivot to other points
            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                d2 = dx*dx + dy*dy       # squared distance
                dist_count[d2] += 1
            
            # For each group of distance d with count c:
            # Add c * (c - 1) boomerangs
            for c in dist_count.values():
                total += c * (c - 1)
        
        return total
