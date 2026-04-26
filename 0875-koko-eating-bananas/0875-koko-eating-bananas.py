class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalHour(piles,hour):
            total_hour = 0
            for i in range(len(piles)):
                total_hour += math.ceil(piles[i]/hour)

            return total_hour
        
        low, high = 1, max(piles)
        ans = high
        while low <= high:
            mid = (low + high)//2
            req_hour = totalHour(piles,mid)
            if req_hour <= h:
                high = mid-1
                ans = min(ans,mid)
            else:
                low = mid+1
        return ans