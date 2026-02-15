class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows , cols = len(image), len(image)
        res = [[0]*rows for _ in range(rows)]   
        for i in range (rows):
            image[i].reverse()
        
        for row in range(rows):
            for col in range (cols):
                if image[row][col] == 0:
                    res[row][col] = 1
                else:
                    res[row][col] = 0
        
        return res


        