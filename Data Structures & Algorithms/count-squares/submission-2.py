class CountSquares:

    def __init__(self):
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None
        self.point_wise_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        point_tuple = tuple(point)
        self.point_wise_count[point_tuple] += 1

        self.min_x = min(self.min_x, point[0]) if self.min_x is not None else point[0]
        self.max_x = max(self.max_x, point[0]) if self.max_x is not None else point[0]
        self.min_y = min(self.min_y, point[1]) if self.min_y is not None else point[1]
        self.max_y = max(self.max_y, point[1]) if self.max_y is not None else point[1]


    def count(self, point: List[int]) -> int:
        ans = 0
        if self.min_x is None:
            return ans
        print(self.point_wise_count)
        for x, y in self.point_wise_count:
            if x == point[0] or point[1] == y:
                continue
            ans += (
                (self.point_wise_count[(x, y)] if (x, y) in self.point_wise_count else 0) *
                (self.point_wise_count[(point[0], y)] if (point[0], y) in self.point_wise_count else 0) *
                (self.point_wise_count[(x, point[1])] if (x, point[1]) in self.point_wise_count else 0)
            )

        return ans