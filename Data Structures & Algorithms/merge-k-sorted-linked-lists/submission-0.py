class MinHeapLL:
    def __init__(self):
        self.head_data = []

    def _is_satisfied(self, parent, child):
        if self.head_data[parent].val < self.head_data[child].val:
            return True
        else:
            return False

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
        if right_child < heap_len and self.head_data[left_child].val > self.head_data[right_child].val:
            small_child = right_child

        if self.head_data[index].val > self.head_data[small_child].val:
            self.head_data[index], self.head_data[small_child] = self.head_data[small_child], self.head_data[index]
            self._heapify_down(small_child)

    def heappush(self, node):
        self.head_data.append(node)
        self._heapify_up(index=len(self.head_data) - 1)

    def heappop(self):
        heap_len = len(self.head_data)
        if heap_len == 0:
            print("Heap Is empty")
            return
        top_node = self.head_data[0]
        last_node = self.head_data.pop()

        if heap_len - 1 > 0:
            self.head_data[0] = last_node
            self._heapify_down(index=0)

        return top_node

    def peek(self):
        if not self.head_data:
            print("Heap is empty")
            return
        return self.head_data[0]



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap_ds = MinHeapLL()
        for ll in lists:
            if ll:
                heap_ds.heappush(ll)

        dummy = ListNode(0)
        curr = dummy

        min_node = heap_ds.heappop()
        while min_node:
            next_node = min_node.next
            curr.next = min_node
            curr = curr.next
            min_node.next = None
            if next_node:
                heap_ds.heappush(next_node)
            min_node = heap_ds.heappop()

        return dummy.next