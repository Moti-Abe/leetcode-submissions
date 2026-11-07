class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [] # pair of position and speed
        stack = deque()
        n = len(speed)
        for i in range(n):
            ps.append((position[i],speed[i]))
        ps.sort()
        
        for i in range (n-1,-1,-1):
            if not stack:
                stack.append(ps[i])
            else:
                if (target - ps[i][0])/ps[i][1] > (target - stack[-1][0])/stack[-1][1]:
                    stack.append(ps[i])
                else:
                    continue
        return len(stack)