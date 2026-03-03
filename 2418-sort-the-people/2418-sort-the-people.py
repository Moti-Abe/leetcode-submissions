class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp = {}
        output = []
        n = len(names)
        for i in range (n):
            mp[heights[i]] = names[i]
        
        
        sorted_mp = dict(sorted(mp.items(),reverse=True))
        
        for height,name in sorted_mp.items():
            output.append(name)
        
        return output