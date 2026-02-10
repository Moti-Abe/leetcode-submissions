class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        output = []

        # iterate over character of the first word
        for c in words[0]:
            ok = True
            
            # check if c exists in all words
            for j in range(len(words)):
                if c not in words[j]:
                    ok = False
                    break
    
            if ok:
                output.append(c)

                # remove one occurence from each word
                for k in range(len(words)):
                    s = list(words[k])
                    s.remove(c)
                    words[k] = "".join(s)
                
        return output
            

               


        