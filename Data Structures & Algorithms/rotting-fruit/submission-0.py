class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 2:
                    continue
                queue.append((i, j))
                visited.add((i, j))
        
        def _add_data(i, j):
            if (i not in range(rows) or j not in range(cols) or (i, j) in visited or  grid[i][j] == 0):
                return
            visited.add((i, j))
            queue.append((i, j))
                
        
        ans = -1
        while queue:
            ans += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                _add_data(i+1, j)
                _add_data(i-1, j)
                _add_data(i, j+1)
                _add_data(i, j-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
        return ans
                
        