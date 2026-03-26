class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left, right = 0, n-1
        count_boat = 0
        
        while left <= right:
            if left == right:
                count_boat += 1
                break
            if people[left] + people[right] <= limit:
                count_boat += 1
                left += 1
                right -= 1
            elif people[left] + people[right] > limit:
                right -= 1
                count_boat += 1


        
        return count_boat
