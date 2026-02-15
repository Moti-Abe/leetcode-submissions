class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        mp = {}
        st = set()
        for i in range (len(arr)):
            char = chr(97+i)
            mp[char] = arr[i]

        for i in range (len(words)):
            s = words[i]
            s = list(s)
            for j in range (len(words[i])):
                s[j] = mp[s[j]]
                
            result_string = "".join(s)
            words[i] = result_string
        
        for word in words:
            st.add(word)
        
        return len(st)
        