class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.size += 1

    def pop(self) -> int:
        ans = None
        for i in range(self.size):
            if i == self.size - 1:
                ans = self.q1.popleft()
                continue
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        self.size -= 1

        return ans


    def top(self) -> int:
        ans = None
        for i in range(self.size):
            if i == self.size - 1:
                ans = self.q1[0]
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

        return ans

    def empty(self) -> bool:
            return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()