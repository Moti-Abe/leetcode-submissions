class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        need_to_cover = [num for num in range(left,right+1)]
        
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                if j in need_to_cover:
                    need_to_cover.remove(j)

        if len(need_to_cover) == 0:
            return True
        else: 
            return False 
        
        