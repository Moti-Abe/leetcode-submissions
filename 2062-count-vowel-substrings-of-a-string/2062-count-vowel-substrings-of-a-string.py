class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        substr = {}
        output = 0
        for i in range (len(word)):
            substr.clear()
            if word[i] not in vowels:
                continue
            for j in range (i, len(word)):
                substr[word[j]] = substr.get(word[j], 0) + 1
                if set(substr) == vowels:
                    output += 1

        return output
            