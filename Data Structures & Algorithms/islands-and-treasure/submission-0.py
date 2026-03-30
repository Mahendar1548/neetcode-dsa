class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(i, j):
            queue = deque()
            visited = set()

            queue.append((i, j))
            visited.add((i, j))

            ans = 0
            while queue:
                ans += 1

                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    for dir in dirs:
                        p = i + dir[0]
                        q = j + dir[1]
                        if p in range(rows) and q in range(cols):
                            if grid[p][q] not in [-1]:
                                if grid[p][q] == 0:
                                    return ans
                                if (p, q) not in visited:
                                    visited.add((p, q))
                                    queue.append((p, q))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] not in [0, -1]:
                    grid[i][j] = bfs(i, j)


