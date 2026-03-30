class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        
        def dfs(start, coin_count):
            # print(dp)
            if start >= amount:
                return 
            
            for coin in coins:
                temp = coin + start
                dp[temp] = min(dp.get(temp, float("inf")), coin_count+1)
                dfs(temp, coin_count+1)
        
        dfs(0, 0)
        return dp[amount] if amount in dp else -1
