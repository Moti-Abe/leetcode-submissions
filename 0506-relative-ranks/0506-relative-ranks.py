class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_pair_index = {}
        for i in range (len(score)):
            score_pair_index[score[i]] = i
        sorted_score_pair_index = dict(sorted(score_pair_index.items(), reverse=True))

        count = 0
        res = [""]*len(score)
        for index, value in sorted_score_pair_index.items():
            count += 1
            if count == 1:
                res[value] = "Gold Medal"
            if count == 2:
                res[value] = "Silver Medal"
            if count == 3:
                res[value] = "Bronze Medal"
            if count > 3:
                res[value] = str(count)
            
            
        return res




        
        