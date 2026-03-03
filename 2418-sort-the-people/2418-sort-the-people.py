class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp = {}
        n = len(names)
        for i in range (n):
            mp[heights[i]] = names[i]
        
        # Buble sort
        items = list(mp.items())
        for i in range (n):
            for j in range (n-1-i):
                if items[j][0] < items[j+1][0]:
                    items[j], items[j+1] = items[j+1], items[j]
        sorted_mp = dict(items)
        
        output = []
        for height,name in sorted_mp.items():
            output.append(name)
        
        return output