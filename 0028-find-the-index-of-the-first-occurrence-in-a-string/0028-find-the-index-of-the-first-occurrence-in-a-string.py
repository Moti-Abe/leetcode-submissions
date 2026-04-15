class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range (len(haystack)):
                if haystack[i] == needle[0]:
                    if haystack[i:i+len(needle)] == needle:
                        return i
        else:
            return -1