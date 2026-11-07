class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loses[loser] = loses.get(loser, 0) + 1

        zero_loses = []
        one_loses = []
        for p in players:
            if p not in loses:
                zero_loses.append(p)
            else:
                if loses[p] == 1:
                    one_loses.append(p)
        
        zero_loses.sort()
        one_loses.sort()
        
        return [zero_loses, one_loses]

