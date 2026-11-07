class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            t.remove(s[i])
        return "".join(t)