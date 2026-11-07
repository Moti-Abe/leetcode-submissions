from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # store (start, original index)
        starts = sorted((intervals[i][0], i) for i in range(n))
        
        result = []
        
        for start, end in intervals:
            idx = bisect_left(starts, (end, -1))
            
            if idx < n:
                result.append(starts[idx][1])
            else:
                result.append(-1)
        
        return result