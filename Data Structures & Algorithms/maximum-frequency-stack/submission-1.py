class FreqStack:

    def __init__(self):
        self.counter = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = max(self.counter.values())
        temp_stack = []
        while self.stack:
            if self.counter[self.stack[-1]] == max_freq:
                max_freq_num = self.stack.pop()
                self.counter[max_freq_num] -= 1
                break
            temp_stack.append(self.stack.pop())
        
        while temp_stack:
            self.stack.append(temp_stack.pop())
        
        return max_freq_num