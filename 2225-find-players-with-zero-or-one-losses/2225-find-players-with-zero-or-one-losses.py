class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer0 = set()
        answer1 = set()
        mp = {}
        for i in range(len(matches)):
            answer0.add(matches[i][0])
            answer1.add(matches[i][1])

        answer_0 = set()
        answer_1 = set()
        for num in answer0:
            if num not in answer1:
                answer_0.add(num)

        for i in range(len(matches)):
            mp[matches[i][1]] = mp.get(matches[i][1], 0) + 1
        
        for key,value in mp.items():
            if value == 1:
                answer_1.add(key)
        
        answer_0 = list(answer_0)
        answer_1 = list(answer_1)
        answer_1.sort()
        answer_0.sort()

        return [answer_0,answer_1]








        