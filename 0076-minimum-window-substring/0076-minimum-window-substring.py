class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        left, right, n = 0, 0, len(s)
        tmp, smp = {}, {}
        min_len = float('inf')
        ind = -1

        for i in range (len(t)):
            tmp[t[i]] = tmp.get(t[i], 0) + 1
        
        

        while right < n:
            smp[s[right]] = smp.get(s[right], 0) + 1
            def isvalid():
                for c in tmp:
                    if tmp[c] > smp.get(c, 0):
                        return False
                return True
            while isvalid():
                if (right - left + 1) <= min_len:
                    ind = left
                    min_len = right - left + 1
                smp[s[left]] -= 1
                left += 1
            right += 1
        
        return "" if ind == -1 else s[ind: ind + min_len]
                
            


        



 

        


                