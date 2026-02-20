class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        res = [[0]*n for _ in range(n)]

        for i in range (n):
            for j in range (n):
                res[i][j] = matrix[j][i]

        for i in range (n):
            for j in range(n//2):
                res[i][j],res[i][n-j-1] = res[i][n-j-1],res[i][j]

        for i in range (n):
            for j in range (n):
                matrix[i][j] = res[i][j]
