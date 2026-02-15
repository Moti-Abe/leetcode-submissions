class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        min_ghost_dif = 1000000
        for i in range(len(ghosts)):
            a = ghosts[i][0] - target[0]
            b = ghosts[i][1] - target[1]
            ghost_dif = abs(a) + abs(b)

            min_ghost_dif = min (min_ghost_dif, ghost_dif)
        
        actual_ghost_dif = abs(0-target[0]) + abs(0-target[1])

        if min_ghost_dif <= actual_ghost_dif:
            return False
        else:
            return True
        
        