class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        current_stock = prices[0]
        
        for price in prices[1:]:
            if current_stock > price:
                current_stock = price
            else:
                profit += price - current_stock
                current_stock = price
        
        return profit