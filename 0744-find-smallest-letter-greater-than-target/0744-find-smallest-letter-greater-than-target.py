class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        n = len(letters)
        low, high = 0, n-1
        ans = 0
        while low <= high:
            mid = (low + high)//2
            if letters[mid] > target:
                high = mid-1
                ans = mid
            else:
                low = mid+1
        
        return letters[ans]