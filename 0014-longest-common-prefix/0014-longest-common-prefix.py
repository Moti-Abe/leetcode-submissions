class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_length = 200
        for i in range(len(strs)):
            min_length = min (min_length, len(strs[i]))

        output = "" 
        for i in range(min_length):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return output 
            output += strs[0][i]
              
        return output

        