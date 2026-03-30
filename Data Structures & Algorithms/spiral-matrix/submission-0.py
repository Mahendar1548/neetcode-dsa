class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        left, top, bottom, right = 0, 0, rows-1, cols-1
    
        response = []
        while left <= right and top <= bottom:
            if left <= right and top <= bottom:
                for i in range(left, right+1):
                    response.append(matrix[top][i])
                top += 1
            if left <= right and top <= bottom:
                for i in range(top, bottom+1):
                    response.append(matrix[i][right])
                right -= 1
            if left <= right and top <= bottom:
                for i in range(right, left-1, -1):
                    response.append(matrix[bottom][i])
                bottom -= 1

            if left <= right and top <= bottom:
                for i in range(bottom, top-1, -1):
                    response.append(matrix[i][left])
                left += 1
            
        return response