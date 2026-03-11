class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        n =len(s)
        left , right = 0, 0
        max_len = 0

        while right < n:
            mp[s[right]] = mp.get(s[right], 0) + 1
            while mp[s[right]] > 1:
                mp[s[left]] -= 1 
                left += 1
                
            
            max_len = max(max_len, right - left + 1)
            
            right += 1
            
        return max_len
 

        