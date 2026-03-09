class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left , right = 0, 0

        output = 0
        while left < len(g) and right <  len(s):
            if g[left] <= s[right]:
                left += 1
                right += 1
                output  += 1
            else:
                right  += 1
        
        return output


        