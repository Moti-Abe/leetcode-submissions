class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        st = []
        st.append(chars[0])
        for i in range (n):
            if chars[i] != st[-1]:
                st.append(chars[i])
    
        res = []
        left = 0
        for i in range (len(st)):
            count = 0
            res.append(st[i])
            
            while left < n and st[i] == chars[left]:
                left += 1 
                count += 1
            if count > 1 and count < 10:
                res.append(str(count))
            elif count > 9:
                temp = list(str(count))
                res = res + temp

        
        m = min(len(chars), len(res))
        
        for i in range (m):
            chars[i] = res[i]
        
        while len(chars) > m:
            chars.pop()

        

        