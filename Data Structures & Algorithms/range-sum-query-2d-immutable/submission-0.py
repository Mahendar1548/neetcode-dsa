class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        prefix_sum_matrix = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(1, len(matrix)+1):
            pref_sum = 0
            for j in range (1, len(matrix[0])+1):
                pref_sum += matrix[i-1][j-1]
                prefix_sum_matrix[i][j] = pref_sum + prefix_sum_matrix[i-1][j]
        self.prefix_sum_matrix = prefix_sum_matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefix_sum_matrix[row2+1][col2+1]
        ans -= self.prefix_sum_matrix[row2+1][col1]
        ans -= self.prefix_sum_matrix[row1][col2+1]
        ans += self.prefix_sum_matrix[row1][col1]
        return ans