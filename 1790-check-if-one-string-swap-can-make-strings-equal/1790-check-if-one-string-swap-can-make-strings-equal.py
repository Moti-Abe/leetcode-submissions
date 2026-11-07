class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        s1 = list(s1)
        s2 = list(s2)
        for i in range(len(s2)):
            if(s1[i] != s2[i]):
                diff.append(i)
        
        if len(diff) == 0:
            return True
        elif len(diff) != 2:
            return False
        
        s2[diff[0]], s2[diff[1]] = s2[diff[1]], s2[diff[0]]

        return s1 == s2

        


        