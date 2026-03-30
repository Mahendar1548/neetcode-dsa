class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_json = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                src, dst = points[i], points[j]
                distance = abs(src[0]-dst[0]) + abs(src[1]-dst[1])
                adj_json[i].append([distance, j])
                adj_json[j].append([distance, i])
        
        min_heap = [[0, 0]]
        visited = set()
        ans = 0
        while len(visited) < len(points):
            min_value = heapq.heappop(min_heap)
            if min_value[1] in visited:
                continue
            
            ans += min_value[0]
            visited.add(min_value[1])
            for neigh in adj_json[min_value[1]]:
                if neigh[1] not in visited:
                    heapq.heappush(min_heap, neigh)
        
        return ans