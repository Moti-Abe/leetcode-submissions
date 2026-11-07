class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {}
        output1 = []
        for i in range (len(arr1)):
            mp[arr1[i]] = mp[arr1[i]] = mp.get(arr1[i], 0) + 1
        
        for i in range(len(arr2)):
            for j in range(mp[arr2[i]]):
                output1.append(arr2[i])
        
        output2 = []
        for i in range (len(arr1)):
            if arr1[i] not in arr2:
                output2.append(arr1[i])
        output2.sort()

        return output1 + output2
        

            
        
          




        