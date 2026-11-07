class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
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
        return res