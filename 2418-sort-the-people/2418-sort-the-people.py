class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        output = []
        people = list(zip(heights,names))
        people.sort(reverse=True)
        
        for height,name in people:
            output.append(name)
        
        return output