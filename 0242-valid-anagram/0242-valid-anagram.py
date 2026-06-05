class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap, tmap = {}, {}
        for c in s:
            smap[c] = s.count(c)
        for c in t:
            tmap[c] = t.count(c)
        
        for key,value in smap.items():
            if key not in tmap or tmap[key] != value:
                return False
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna