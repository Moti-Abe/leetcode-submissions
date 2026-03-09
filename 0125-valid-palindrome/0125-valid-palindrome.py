class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = list(s)
        res = []
        for i in range (len(s)):
            s[i] = s[i].lower()
            if (s[i].isalnum()):
                res.append(s[i])
        
        res = "".join(res)

        reversed_res = res[::-1]

        if res == reversed_res:
            return True
        else:
            return False
        