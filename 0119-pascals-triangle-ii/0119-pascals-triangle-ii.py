class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1,1])
            else:
                arr = deque()
                for j in range (i-1):
                    arr.append(res[i-1][j]+res[i-1][j+1])
                arr.append(1)
                arr.appendleft(1)
                res.append(list(arr))
        return res[-1]