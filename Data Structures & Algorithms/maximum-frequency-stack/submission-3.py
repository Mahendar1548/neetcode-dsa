class FreqStack:

    def __init__(self):
        self.stacks = [[]]
        self.element_wise_count = defaultdict(int)

    def push(self, val: int) -> None:
        self.element_wise_count[val] += 1
        val_freq = self.element_wise_count[val]
        
        if val_freq == len(self.stacks):
            self.stacks.append([])
        
        self.stacks[val_freq].append(val)


    def pop(self) -> int:
        ans = self.stacks[-1].pop()
        self.element_wise_count[ans] -= 1
        
        if not self.stacks[-1]:
            self.stacks.pop()
        
        return ans