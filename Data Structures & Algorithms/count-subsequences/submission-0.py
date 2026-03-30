class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = dict()

        def dfs(i, j):
            if j == len(t):
                return 1
            
            if i >= len(s):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]
            
            value = dfs(i+1, j) + (dfs(i+1, j+1) if s[i] == t[j] else 0)
            dp[(i, j)] = value
            return value
        
        return dfs(0, 0)
        