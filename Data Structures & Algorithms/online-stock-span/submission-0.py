class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        
        if self.stack:
            span = len(self.prices) - (self.stack[-1] + 1)
        else:
            span = len(self.prices)
        
        self.stack.append(len(self.prices)-1)
        return span