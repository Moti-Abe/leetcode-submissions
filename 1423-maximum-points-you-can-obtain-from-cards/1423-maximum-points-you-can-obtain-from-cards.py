class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right =  len(cardPoints) - k, 0
        total, max_points = 0, 0
        for i in range(left, len(cardPoints)):
            total += cardPoints[i]
        
        while right <= k:
            max_points = max(max_points, total)
            if right == k:
                break
            total -= cardPoints[left]
            left += 1
            total += cardPoints[right]
            right += 1
        
        return max_points