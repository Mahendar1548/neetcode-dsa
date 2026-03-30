class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], (0, 0))]
        grid_size = len(grid)
        
        visited = set()
        
        while min_heap:
            time, point = heapq.heappop(min_heap)
            if point in visited:
                continue

            if point == (grid_size-1, grid_size-1):
                return time
            
            visited.add(point)

            if point[0] + 1 < grid_size and (point[0] + 1, point[1]) not in visited:
                heapq.heappush(min_heap, (max(time, grid[point[0] + 1][point[1]]), (point[0] + 1, point[1])))
            
            if point[0] - 1 >= 0 and (point[0] - 1, point[1]) not in visited:
                heapq.heappush(min_heap, (max(time, grid[point[0] - 1][point[1]]), (point[0] - 1, point[1])))
            
            if point[1] - 1 >= 0 and (point[0], point[1] - 1) not in visited:
                heapq.heappush(min_heap, (max(time, grid[point[0]][point[1]-1]), (point[0], point[1]-1)))
            
            if point[1] + 1 < grid_size and (point[0], point[1] + 1) not in visited:
                heapq.heappush(min_heap, (max(time, grid[point[0]][point[1]+1]), (point[0], point[1]+1)))