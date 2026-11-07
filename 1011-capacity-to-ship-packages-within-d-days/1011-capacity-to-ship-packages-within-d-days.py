class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def required_days(weights, capacity):
            day, load = 1, 0
            for i in range(len(weights)):
                if load + weights[i] > capacity:
                    day += 1
                    load = weights[i]
                else:
                    load += weights[i]
            
            return day

        #O(nlogn)
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low+high)//2
            daysReq = required_days(weights, mid)
            if daysReq <= days:
                high = mid-1
            else:
                low = mid+1
        return low

        # O(n^2)
        # for cap in range(max_weight,total):
        #     daysReq = required_days(weights, cap)
        #     if daysReq <= days:
        #         return cap
