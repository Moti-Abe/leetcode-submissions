class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        mp = {}
        
        for i in range(len(pick)):
            pick[i] = tuple(pick[i])
            mp[pick[i]] = mp.get(pick[i], 0) + 1
        st = set(pick)
        res = set()
        
        arr = list(st)
        count = 0
        for i in range (len(arr)):
            if arr[i][0] < mp[arr[i]]:
                res.add(arr[i][0])

        return len(res)