class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        output = 0
        for i in range (len(seats)):
            moves = abs(seats[i] - students[i])
            output += moves
        
        return output
        