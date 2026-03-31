class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.tail = None
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        if self.tail is None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.tail.next = self.head
        self.size += 1
        return True


    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        if self.size == 1:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k