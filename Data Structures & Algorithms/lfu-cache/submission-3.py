class DLNode:
    def __init__(self, key, val, freq):
        self.val = val
        self.freq = freq
        self.key = key
        self.prev = None
        self.next = None

    def __str__(self):
        data = []
        start = self
        current = self
        while current.next != start:
            data.append(current.val)
            current = current.next

        data.append(current.val)
        return "->".join([str(each) for each in data])


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.least_freq = 0
        self.key_wise_node = dict()
        self.freq_wise_head = dict()

    def _delete_node(self, node: DLNode):
        freq = node.freq
        freq_head = self.freq_wise_head[freq]
        if freq_head == freq_head.prev:
            self.freq_wise_head[freq] = None
        else:
            if freq_head == node:
                self.freq_wise_head[freq] = freq_head.next
            node.next.prev = node.prev
            node.prev.next = node.next

        node.prev = node.next = None
        self.curr_size -= 1

    def _add_node(self, node: DLNode):
        freq = node.freq
        freq_head = self.freq_wise_head.get(freq, None)
        if freq_head is None:
            self.freq_wise_head[freq] = node
            node.next = node.prev = node
        else:
            last_node = freq_head.prev
            last_node.next = node
            node.prev = last_node
            node.next = freq_head
            freq_head.prev = node
        self.curr_size += 1

    def get(self, key: int) -> int:
        if key not in self.key_wise_node:
            return -1

        node = self.key_wise_node[key]
        self._delete_node(node)
        if self.least_freq == node.freq:
            if self.freq_wise_head[node.freq] is None:
                self.least_freq += 1
        node.freq += 1
        self._add_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        need_to_invalidate = False
        if key not in self.key_wise_node:
            if self.curr_size == self.capacity:
                need_to_invalidate = True

        if need_to_invalidate:
            least_freq_head = self.freq_wise_head[self.least_freq]
            print(f"invalidating {least_freq_head.val} node")
            self._delete_node(least_freq_head)
            del self.key_wise_node[least_freq_head.key]

        if key in self.key_wise_node:
            self.get(key)
            self.key_wise_node[key].val = value
        else:
            new_node = DLNode(key, value, 1)
            self.least_freq = 1
            self._add_node(new_node)
            self.key_wise_node[key] = new_node