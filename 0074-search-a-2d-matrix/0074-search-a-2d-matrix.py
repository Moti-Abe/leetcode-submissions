class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [item for sublist in matrix for item in sublist]
        low, high = 0, len(flat_list) - 1
        
        while low <= high:
            mid = (low+high)//2
            if flat_list[mid] < target:
                low = mid+1
            elif flat_list[mid] > target:
                high = mid - 1
            else:
                return True
        
        return False

