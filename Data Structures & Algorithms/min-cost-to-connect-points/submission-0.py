class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ans = 0
        visited = [points[0]]
        for point in points:
            min_value = float("inf")
            for each in visited:
                min_value = min(min_value, (abs(each[0]-point[0]) + abs(each[1]-point[1])))
            ans += min_value
            visited.append(point)
        
        return ans