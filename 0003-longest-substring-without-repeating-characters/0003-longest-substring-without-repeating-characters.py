class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        n = len(s)
        max_len = 0
        left , right = 0, 0

        while right < n:
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
            
        return max_len
 

        