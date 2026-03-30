class DLLNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_wise_value = dict()
        self.last = None
        self.head = None
        self.key_wise_node = dict()

    def get(self, key: int) -> int:
        if key not in self.key_wise_value:
            return -1

        node = self.key_wise_node[key]
        self._move_node_to_last(node)

        return self.key_wise_value[key]

    def _move_node_to_last(self, node):
        node_left = node.left
        node_right = node.right
        if node_right and node_left:
            node_right.left = node_left
            node_left.right = node_right
            node.left = node.right = None
            self.last.right = node
            node.left = self.last
        elif node_right:
            node_right.left = node_left
            node.left = self.last
            node.right = None
            self.head = node_right
        self.last = node

    def put(self, key: int, value: int) -> None:
        if key in self.key_wise_value:
            node = self.key_wise_node[key]
            self._move_node_to_last(node)
        else:
            if self.capacity == 0:
                del self.key_wise_value[self.head.value]
                self.head.right.left = None
                self.head = self.head.right
                self.capacity += 1
            new_node = DLLNode(key)
            if self.last:
                self.last.right = new_node
                new_node.left = self.last
            self.last = new_node
            if not self.head:
                self.head = new_node
            self.key_wise_node[key] = new_node
            self.capacity -= 1
        self.key_wise_value[key] = value