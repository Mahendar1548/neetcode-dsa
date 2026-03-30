class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, visited):
            if not 0 <= r < rows or not 0 <= c < cols or (r, c) in visited or board[r][c] == "X":
                return

            visited.add((r, c))

            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    connected = set()
                    dfs(i, j, connected)
                    any_edge = False
                    for each in connected:
                        if each[0] in [0, rows-1] or each[1] in [0, cols-1]:
                            any_edge = True
                            break
                    if any_edge:
                        continue
                    for each in connected:
                        board[each[0]][each[1]] = "X"