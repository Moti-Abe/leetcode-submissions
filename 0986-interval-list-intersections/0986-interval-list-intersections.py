class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        output = []

        while l < len(firstList)-1 and r < len(secondList)-1:
            if firstList[l][0] <= secondList[r][0] <= firstList[l][1]:
                interval = [secondList[r][0], min(secondList[r][1], firstList[l][1])]
                output.append(interval)
            elif firstList[l][0] >= secondList[r][0] and firstList[l][0] <= secondList[r][1]:
                interval = [firstList[l][0], min(secondList[r][1], firstList[l][1])]
                output.append(interval)
            
            if secondList[r+1][0] > firstList[l+1][0]:
                l += 1
            else:
                r += 1
        
        while l == len(firstList)-1 and r < len(secondList)-1:
            if firstList[l][0] <= secondList[r][0] <= firstList[l][1]:
                interval = [secondList[r][0], min(secondList[r][1], firstList[l][1])]
                output.append(interval)
            elif firstList[l][0] >= secondList[r][0] and firstList[l][0] <= secondList[r][1]:
                interval = [firstList[l][0], min(secondList[r][1], firstList[l][1])]
                output.append(interval)
            
            r += 1
        
        while l < len(firstList)-1 and r == len(secondList)-1:
            if firstList[l][0] <= secondList[r][0] <= firstList[l][1]:
                interval = [secondList[r][0], min(secondList[r][1], firstList[l][1])]
                output.append(interval)
            elif firstList[l][0] >= secondList[r][0] and firstList[l][0] <= secondList[r][1]:
                interval = [firstList[l][0], min(secondList[r][1], firstList[l][1])]
                output.append(interval)
            
            l += 1
            
        if l < len(firstList) and r < len(secondList):
            if firstList[l][0] <= secondList[r][0] <= firstList[l][1]:
                interval = [secondList[r][0], min(secondList[r][1], firstList[l][1])]
                output.append(interval)
            elif firstList[l][0] >= secondList[r][0] and firstList[l][0] <= secondList[r][1]:
                interval = [firstList[l][0], min(secondList[r][1], firstList[l][1])]
                output.append(interval)   

        return output
        