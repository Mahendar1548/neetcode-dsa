class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()
        ans = 0

        def dfs(day, action, profit, buy_value):
            nonlocal ans
    
            if day >= len(prices):
                ans = max(ans, profit)
                return 
            
            if action == 1:
                dfs(day+1, action, profit, buy_value)
                dfs(day+1, -1, profit, prices[day])
            else:
                dfs(day + 1, action, profit, buy_value)
                dfs(day+2, 1, profit + (prices[day] - buy_value), None)
        
        dfs(0, 1, 0, None)
        return ans