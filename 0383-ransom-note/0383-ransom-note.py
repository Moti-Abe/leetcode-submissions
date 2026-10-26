class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note = {}
        for c in ransomNote:
            ransom_note[c] = ransom_note.get(c, 0) + 1

        mag = {}
        for m in magazine:
            mag[m] = mag.get(m, 0) + 1
        
        for r in ransomNote:
            if r not in mag:
                return False
            if r in mag and ransom_note[r] > mag[r]:
                return False
        return True