class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols:
                return False

            if board[r][c] == "X":
                return True

            board[r][c] = "X"
            ans = all([dfs(r+1, c), dfs(r-1, c), dfs(r, c+1), dfs(r, c-1)])
            if not ans:
                board[r][c] = "O"
            
            return ans
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    dfs(i, j)
