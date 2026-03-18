class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mp = {}
        left, right = 0, 0
        max_fruits  = 0
        while right < len(fruits):
            mp[fruits[right]] = mp.get(fruits[right], 0) + 1

            while len(mp) > 2:
                mp[fruits[left]] -= 1
                if mp[fruits[left]] == 0:
                    del mp[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
            right += 1
        
        return max_fruits