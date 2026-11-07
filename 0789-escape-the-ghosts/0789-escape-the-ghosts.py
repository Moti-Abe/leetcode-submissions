class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        min_ghost_distance = 1000000
        for i in range(len(ghosts)):
            x_axis_ghost_distance = ghosts[i][0] - target[0]
            y_axis_ghost_distance = ghosts[i][1] - target[1]
            ghost_distance = abs(x_axis_ghost_distance) + abs(y_axis_ghost_distance)

            min_ghost_distance = min(min_ghost_distance, ghost_distance)
        
        player_distance = abs(0-target[0]) + abs(0-target[1])

        if min_ghost_distance <= player_distance:
            return False
        else:
            return True
        
        