class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range (9):
            arr1 = []
            arr2 = []
            for j in range (9):
                if board[i][j].isdigit():
                    arr1.append(board[i][j])
                
                if board[j][i].isdigit():
                    arr2.append(board[j][i])

            if len(arr1) != len(set(arr1)):
                return False
            if len(arr2) != len(set(arr2)):
                return False

        for r in range(0,9,3):
            for c in range(0,9,3):
                arr = []
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j].isdigit():
                            arr.append(board[r+i][c+j])
                
                if len(arr) != len(set(arr)):
                    return False
        
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna