class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        left, right = 0, 0
        players.sort()
        trainers.sort()
        output = 0
        while  left < len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                output += 1
                left += 1
                right += 1
            else:
                right += 1
        return output

        