class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        output = []
        for i in range (len(words)):
            count1, count2, count3 = 0, 0, 0
            for j in range (len(words[i])):
                word = words[i]
                word = word.lower()
                if word[j] in "qwertyuiop":
                    count1 += 1
                elif word[j] in "asdfghjkl":
                    count2 += 1
                elif word[j] in "zxcvbnm":
                    count3 += 1
            
            count = max(count1, count2, count3)
                 
            if count == len(word):
                output.append(words[i])
            
        return output