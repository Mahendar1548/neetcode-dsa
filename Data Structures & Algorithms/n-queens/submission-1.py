class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        curr = []

        def backtrack(i):
            if i >= n:
                ans.append(curr.copy())
                return

            for j in range(n):
                if self._check_it_works(curr, j, n):
                    curr.append(j)
                    backtrack(i+1)
                    curr.pop()
        backtrack(0)
        return self._generate_queens_on_chess_board(ans, n)

    def _check_it_works(self, existing, new_col, n):
        if new_col in existing:
            return False
        curr_row = len(existing)
        for i in range(len(existing)):
            if abs(curr_row - i) == abs(new_col - existing[i]):
                return False

        return True

    def _generate_queens_on_chess_board(self, nums_queens, n):
        res = []
        for board in nums_queens:
            curr_board = []
            for value in board:
                temp = ["."] * n
                temp[value] = "Q"
                curr_board.append("".join(temp))
            res.append(curr_board)

        return res
