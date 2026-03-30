class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = dict()

        def dfs(idx, sum_val):
            if (idx, sum_val) in dp:
                return dp[(idx, sum_val)]
    
            if sum_val == amount:
                return 1
            if sum_val > amount:
                return 0
    
            times = 0
            for i in range(idx, len(coins)):
                times += dfs(i, sum_val+coins[i])
            
            dp[(idx, sum_val)] = times
            return dp[(idx, sum_val)]

        return dfs(0, 0)
