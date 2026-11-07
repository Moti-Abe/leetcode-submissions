class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp = {}
        n = len(names)
        for i in range (n):
            mp[heights[i]] = names[i]
        
        # Selection Sort
        items = list(mp.items())
        for i in range (n-1,-1,-1):
            minpos = i
            for j in range (i-1,-1,-1):
                if items[j][0] < items[minpos][0]:
                    minpos = j
            items[i],items[minpos] = items[minpos], items[i]
        sorted_mp = dict(items)
        
        output = []
        for height,name in sorted_mp.items():
            output.append(name)
        
        return output