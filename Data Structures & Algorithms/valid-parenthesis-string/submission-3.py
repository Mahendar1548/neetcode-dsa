class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = dict()
        def dfs(idx, balance):
            if (idx, balance) in dp:
                return dp[(idx, balance)]
            if balance < 0:
                return False
            if idx == len(s):
                return balance == 0
            if s[idx] == "(":
                ans = dfs(idx+1, balance+1)
            elif s[idx] == ")":
                ans = dfs(idx+1, balance-1)
            else:
                ans = dfs(idx+1, balance-1) or dfs(idx+1, balance-1) or dfs(idx+1, balance)
            
            dp[(idx, balance)] = ans
            return ans
        
        return dfs(0, 0)
