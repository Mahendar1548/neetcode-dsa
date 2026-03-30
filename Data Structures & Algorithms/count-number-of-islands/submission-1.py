class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            visited.add((i, j))
            
            q = deque()
            q.append((i, j))
            
            while q:
                i, j = q.popleft()
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for k, l in dirs:
                    m = i + k
                    n  = j + l
                    if m in range(rows) and n in range(cols) and (m, n) not in visited:
                        if grid[m][n] == "1":
                            visited.add((m, n))
                            q.append((m, n))

        ans = 0
        for a in range(rows):
            for b in range(cols):
                if grid[a][b] == "1" and (a, b) not in visited:
                    print("Hi")
                    bfs(a, b)
                    ans += 1

        return ans
