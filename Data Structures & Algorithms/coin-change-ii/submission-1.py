class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = 0
        comb = []
        def dfs(idx, sum_val):
            nonlocal ans

            if sum_val == amount:
                # print(comb)
                ans = ans + 1
                return 
            if sum_val > amount:
                return
            
            for i in range(idx, len(coins)):
                comb.append(coins[i])
                dfs(i, sum_val+coins[i])
                comb.pop()
        dfs(0, 0)
        return ans