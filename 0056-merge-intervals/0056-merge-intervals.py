class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        current = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= current[1]:
                current[1] = max(current[1], intervals[i][1])
            else:
                output.append(current)
                current = intervals[i]
        output.append(current)
        return output


        