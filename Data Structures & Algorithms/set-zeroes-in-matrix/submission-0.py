class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        has_fr_not_zero = all(matrix[0])
        has_fc_not_zero = all([matrix[i][0] for i in range(len(matrix))])

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if not has_fr_not_zero:
            for i in range(0, cols):
                matrix[0][i] = 0
        if not has_fc_not_zero:
            for i in range(0, rows):
                matrix[i][0] = 0