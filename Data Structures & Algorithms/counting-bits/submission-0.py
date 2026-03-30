class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        dp = [0, 1]
        times, curr = len(dp), 0
        value = 1
        for i in range(2, n+1):
            dp.append(value+dp[curr])
            times -= 1
            curr += 1
            if times == 0:
                value, curr, times = 1, 0, len(dp)
        
        return dp
