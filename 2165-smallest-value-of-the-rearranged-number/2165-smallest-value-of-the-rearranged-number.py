class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num < 0:
            s = list(str(num))
            s.remove('-')
            s.sort(reverse=True)
            num = int("".join(s))
            num = -1*num
        elif num > 0:
            s = list(str(num))
            unique = list(set(s))
            unique.sort()
            s.sort()
            if s[0] == '0':
                i = s.index(unique[1])
                s[0], s[i] = unique[1],s[0]
            num = int("".join(s))
        else:
            num = 0
        
        return num
            



        
        