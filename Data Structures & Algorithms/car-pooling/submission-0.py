class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []
        for p_num, start, dest in trips:
            points.append((start, p_num))
            points.append((dest, -p_num))

        heapq.heapify(points)
        current = 0
        while points:
            _, p_num = heapq.heappop(points)
            current += p_num
            if current > capacity:
                return False
        
        return True