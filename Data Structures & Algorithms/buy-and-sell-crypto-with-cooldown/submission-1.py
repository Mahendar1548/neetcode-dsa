
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()

        def dfs(day, buying):
            if day >= len(prices):
                return 0

            if (day, buying) in dp:
                return dp[(day, buying)]
    
            calm = dfs(day+1, buying)
            if buying:
                buy_value = dfs(day+1, not buying) - prices[day]
                dp[(day, buying)] = max(calm, buy_value)
            else:
                sell_value = dfs(day + 2, not buying) + prices[day]
                dp[(day, buying)] = max(calm, sell_value)
            
            return dp[(day, buying)]

        return dfs(0, True)
