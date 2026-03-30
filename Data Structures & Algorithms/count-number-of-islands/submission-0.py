class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i not in range(rows) or j not in range(cols):
                return
            if grid[i][j] == "0" or (i,j) in visited:
                return

            visited.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        ans = 0
        for a in range(rows):
            for b in range(cols):
                if grid[a][b] == "1" and (a, b) not in visited:
                    print("Hi")
                    dfs(a, b)
                    ans += 1

        return ans
