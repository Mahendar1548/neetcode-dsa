class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix)

        times = rows // 2
        for i in range(times):
            for j in range(i, cols-1-i):
                temp = matrix[j][cols-1-i]
                matrix[j][cols-1-i] = matrix[i][j]
                
                temp2 = matrix[cols-1-i][cols-1-j]
                matrix[cols-1-i][cols - 1 - j] = temp
                
                temp = matrix[cols - 1 - j][i]
                matrix[cols - 1 - j][i] = temp2
                
                matrix[i][j] = temp
                print(matrix)
        