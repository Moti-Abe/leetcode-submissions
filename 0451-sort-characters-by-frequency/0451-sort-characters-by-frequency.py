class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        s = list(s)
        res = []
        for i in range (len(s)):
            mp[s[i]] = mp.get(s[i],0) + 1
        
        sorted_mp = dict(sorted(mp.items(), key=lambda x:x[1], reverse=True))
        for key, value in sorted_mp.items():
            for i in range (value):
                res.append(key)
        
        return "".join(res)



        