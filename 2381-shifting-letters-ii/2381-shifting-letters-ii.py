class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s)+1)
        for l,r,d in shifts:
            if d == 1:
                prefix[r+1] += 1
                prefix[l] -= 1
            else:
                prefix[r+1] -= 1 
                prefix[l] += 1
        
        diff = 0
        # convert string chars to numbers
        res = []
        for c in s:
            res.append(ord(c) - ord("a"))
        
        for i in range(len(prefix)-1, 0, -1):
            diff += prefix[i]
            value = res[i-1]
            value = (value + diff + 26) % 26

            res[i-1] = value
        
        ans = []
        for n in res:
            ans.append(chr(ord("a") + n))
        
        return "".join(ans)