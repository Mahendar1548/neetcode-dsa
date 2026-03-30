class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            visited.add((i, j))

            q = deque()
            q.append((i, j))
            res = 0

            while q:
                res += 1
                i, j = q.popleft()
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for k, l in dirs:
                    m = i + k
                    n  = j + l
                    if m in range(rows) and n in range(cols) and (m, n) not in visited:
                        if grid[m][n]:
                            visited.add((m, n))
                            q.append((m, n))
            
            return res

        ans = 0
        for a in range(rows):
            for b in range(cols):
                if grid[a][b] and (a, b) not in visited:
                    ans  = max(ans, bfs(a, b))

        return ans
