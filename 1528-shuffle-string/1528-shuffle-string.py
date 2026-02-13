class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mp = {}
        res = []
        for i in range (len(s)):
            mp[indices[i]] = s[i]
        sorted_mp = dict(sorted(mp.items()))

        for value in sorted_mp.values():
            res.append(value)
        
        return "".join(res)


        