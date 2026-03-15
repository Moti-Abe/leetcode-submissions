class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1dict = {}
        for i in range (len(s1)):
            s1dict[s1[i]] = s1dict.get(s1[i], 0) + 1
        
        s2dict = {}
        left, right = 0, 0
        istrue = False
        while right < len(s2):
            
            s2dict[s2[right]] = s2dict.get(s2[right], 0) + 1
            if right - left + 1 > len(s1):
                s2dict[s2[left]] -= 1
                if s2dict[s2[left]] == 0:
                    del s2dict[s2[left]]
                left += 1
            
            if s1dict == s2dict:
                istrue = True
                break
            
            right += 1
        
        return istrue

        

        