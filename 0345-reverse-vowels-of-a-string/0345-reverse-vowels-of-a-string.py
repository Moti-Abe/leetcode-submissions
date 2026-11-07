class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        l, r = 0, len(s)-1
        res = list(s)
        while l < r:
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1
            if s[l] in vowels and s[r] in vowels:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
        return "".join(res)