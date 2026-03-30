class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t)+1) for i in range(len(s)+1)]
        dp[len(s)][len(t)] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(len(t), -1, -1):
                value = dp[i+1][j]
                if 0 <= j <len(t) and s[i] == t[j]:
                    value += dp[i+1][j+1]
                
                dp[i][j] = value
        
        return dp[0][0]