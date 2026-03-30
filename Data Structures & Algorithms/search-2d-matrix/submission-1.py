class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        low, high = 0, (rows*cols) - 1
        
        while low <= high:
            mid = (low + high) // 2
            curr_row = mid // cols
            curr_col = mid % cols
            if target == matrix[curr_row][curr_col]:
                return True
            elif target > matrix[curr_row][curr_col]:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
