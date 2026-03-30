import _heapq


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.distance = math.sqrt(x ** 2 + y ** 2)

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def get_point(self):
        return [self.x, self.y]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            point_obj = Point(*point)
            heapq.heappush(heap, point_obj)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap).get_point())
        
        return ans
