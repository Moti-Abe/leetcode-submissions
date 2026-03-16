class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mp = {'B':0, 'W':0}
        for i in range (k):
            mp[blocks[i]] += 1
        
        left , right = 0, k
        min_num = float('inf')
        while right <= len(blocks):
            min_num = min(min_num, mp['W'])
            if right == len(blocks):
                break
            mp[blocks[left]] -= 1
            mp[blocks[right]] += 1
            left += 1
            right += 1
        
        if len(blocks) == k:
            min_num = min(min_num, mp['W'])
        return min_num



