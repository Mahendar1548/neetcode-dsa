class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        land = 2147483647
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        level = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i, new_j = i+dx, j +dy
                    if 0 > new_i or 0 > new_j or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] == -1 or (new_i, new_j) in visited:
                        continue
                    grid[new_i][new_j] = level
                    q.append((new_i, new_j))
                    visited.add((new_i, new_j))
            level += 1