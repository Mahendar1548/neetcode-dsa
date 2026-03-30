class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()

                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for k, l in dirs:
                    p, q = i+k, j+l
                    if (p in range(rows) and q in range(cols) and (p, q) not in visited
                            and grid[p][q] != -1):
                        grid[p][q] = distance
                        queue.append((p, q))
                        visited.add((p, q))