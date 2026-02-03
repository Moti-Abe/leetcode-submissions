class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        need_to_cover = set(range(left, right+1))
        
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                if j in need_to_cover:
                    need_to_cover.discard(j)

        # returns true if set is empty which means all ranges are covered
        return len(need_to_cover) == 0
        
        