class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        left, right, count = 0, 0, 0
        max_vowels = 0
        while right < len(s):
            if s[right] in vowels:
                count += 1
            max_vowels = max(max_vowels, count)
            if max_vowels == k:
                break
            if (right - left + 1) == k:
                if s[left] in vowels:
                    count -= 1
                left += 1
            
            right += 1 
        
        return max_vowels
