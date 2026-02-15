class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp1, mp2 = {}, {}
        for i in range (len(list1)):
            mp1[list1[i]] = i 
        for i in range (len(list2)):
            mp2[list2[i]] = i 

        min_index = 3000

        output = []
        for string in list1:
            if string in list2:
                index = mp1[string] + mp2[string]

                if index < min_index:
                    output.clear()
                    min_index = index
                    output.append(string)
                elif index == min_index:
                    output.append(string)
    
        return output


    
        
        