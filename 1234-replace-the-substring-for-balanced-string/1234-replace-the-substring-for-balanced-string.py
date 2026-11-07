class Solution:
    def balancedString(self, s: str) -> int:
        chars = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        temp = {}
        mp = {}
        l, r = 0, 0
        min_len = float('inf')
        balanced = int(len(s)/4)

        for i in range(len(s)):
            chars[s[i]] += 1
        
        for key, value in chars.items():
            if value > balanced:
                mp[key] = (value - balanced)

        if len(mp) == 0:
            return 0
        
        def isvalid():
            for c in mp:
                if temp.get(c,0) < mp[c]:
                    return False
            return True
        
        while r < len(s):
            if s[r] in mp:
                temp[s[r]] = temp.get(s[r], 0) + 1

            while isvalid() and l <= r:
                min_len = min(min_len, r-l+1)
                if s[l] in mp:
                    temp[s[l]] -= 1
                l += 1
            r += 1
        
        return min_len
        


