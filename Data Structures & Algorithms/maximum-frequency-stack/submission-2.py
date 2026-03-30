class FreqStack:

    def __init__(self):
        self.min_heap = []
        self.count = 0
        self.element_wise_count = defaultdict(int)

    def push(self, val: int) -> None:
        self.element_wise_count[val] += 1
        self.count += 1
        heapq.heappush(self.min_heap, (-self.element_wise_count[val], -self.count, val))


    def pop(self) -> int:
        max_freq_value = heapq.heappop(self.min_heap)
        value = max_freq_value[2]
        self.element_wise_count[value] -= 1
        return value