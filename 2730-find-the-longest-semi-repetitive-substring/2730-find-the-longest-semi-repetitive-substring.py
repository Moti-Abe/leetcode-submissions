class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_len = 1
        n = len(s)
        l = 0
        pairs = 0
        for r in range(1,n):
            if s[r] == s[r-1]:
                pairs += 1
            
            while pairs > 1:
                if s[l] == s[l+1]:
                    pairs -= 1
                l += 1 
            
            max_len = max(max_len, r-l+1)
            
            
        return max_len