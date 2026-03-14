class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        left, right = 0, 0
        pdict, sdict = {}, {}

        if len(s) < len(p):
            return []

        for i in range (len(p)):
            pdict[p[i]] = pdict.get(p[i], 0) + 1
            sdict[s[right]] = sdict.get(s[right], 0) + 1
            right += 1

        for right in range(len(p), len(s)):
            if pdict == sdict:
                output.append(left)

            sdict[s[right]] = sdict.get(s[right], 0) + 1
            
            sdict[s[left]] -= 1
            if sdict[s[left]] == 0:
                del sdict[s[left]]
            left += 1
            
            right += 1

        if pdict == sdict:
            output.append(left)
        
        return output

        