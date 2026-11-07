class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = []
        for i in range(1,n+1):
            circle.append(i)
        
        index = 0
        while len(circle) > 1:
            index = (index + k - 1)% len(circle)
            circle.remove(circle[index])
        
        return circle[0]



        
        