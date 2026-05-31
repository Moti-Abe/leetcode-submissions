class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_len = 0
        if len(s) <3:
            return len(s)
        for i in range(len(s)):
            count = 0
            for j in range(i+1,len(s)):
                if s[j] == s[j-1]:
                    count += 1
                if count == 2:
                    max_len = max(max_len, j-i)
                    break
                
                max_len = max(max_len, j-i+1)

        return max_len