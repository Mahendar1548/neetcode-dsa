class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        bucket_key = key % 1000
        curr_node = self.hashmap[bucket_key]
        prev = None
        while curr_node:
            if curr_node.key == key:
                curr_node.value = value
                return
            prev = curr_node
            curr_node = curr_node.next
    
        prev.next = ListNode(key, value)

    def get(self, key: int) -> int:
        bucket_key = key % 1000
        curr_node = self.hashmap[bucket_key]
        
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        
        return -1

    def remove(self, key: int) -> None:
        bucket_key = key % 1000
        curr_node = self.hashmap[bucket_key]
        prev = None
        while curr_node:
            if curr_node.key == key:
                prev.next = curr_node.next
                return
            prev = curr_node
            curr_node = curr_node.next

class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next
