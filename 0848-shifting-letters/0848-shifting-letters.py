class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        for i in range (1,n):
            shifts[i] += shifts[i-1] 
        shifts.insert(0,0)
        
        for i in range (n):
            shifts[i] = shifts[-1] - shifts[i]
        shifts.pop()
    
        s = list(s)
        for i in range(n):
            shift = shifts[i] % 26
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            s[i] = chr(new_char + ord('a'))
                              
        return "".join(s)

