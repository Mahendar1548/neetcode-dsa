class MinHeap:
    def __init__(self, nums):
        self.head_data = nums

    def _is_satisfied(self, parent, child):
        if self.head_data[parent] < self.head_data[child]:
            return True
        else:
            return False

    def heapify(self):
        heap_half_len = len(self.head_data) // 2
        for i in range(heap_half_len-1, -1, -1):
            self._heapify_down(index=i)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and not self._is_satisfied(parent=parent, child=index):
            self.head_data[parent], self.head_data[index] = self.head_data[index], self.head_data[parent]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left_child = index * 2 + 1
        right_child = index * 2 + 2

        heap_len = len(self.head_data)

        if not left_child < heap_len:
            return

        small_child = left_child
        if right_child < heap_len and self.head_data[left_child] > self.head_data[right_child]:
            small_child = right_child

        if self.head_data[index] > self.head_data[small_child]:
            self.head_data[index], self.head_data[small_child] = self.head_data[small_child], self.head_data[index]
            self._heapify_down(small_child)

    def heappush(self, value):
        self.head_data.append(value)
        self._heapify_up(index=len(self.head_data) - 1)

    def heappop(self):
        heap_len = len(self.head_data)
        if heap_len == 0:
            print("Heap Is empty")
            return
        top_value = self.head_data[0]
        last_value = self.head_data.pop()

        if heap_len - 1 > 0:
            self.head_data[0] = last_value
            self._heapify_down(index=0)

        return top_value
    
    def peek(self):
        if not self.head_data:
            print("Heap is empty")
            return 
        return self.head_data[0]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap_ds = MinHeap(nums=nums)

        for i in range(len(nums)-k):
            self.heap_ds.heappop()

    def add(self, val: int) -> int:
        self.heap_ds.heappush(value=val)
        self.heap_ds.heappop()
        return self.heap_ds.peek()

