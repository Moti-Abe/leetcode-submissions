class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        l, r = 0, n-1
        r_max = n
        while colors[l] == colors[r]:
            r -= 1
            r_max -= 1

        l, r = 0, n-1
        l_max = n
        while colors[l] == colors[r]:
            l += 1
            l_max -= 1
        
        return max(l_max, r_max)-1