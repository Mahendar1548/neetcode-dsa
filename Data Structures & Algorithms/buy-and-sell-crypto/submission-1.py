class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        max_right = prices[prices_len-1]
        ans = 0
        for i in range(prices_len-2, -1, -1):
            ans = max(ans, max_right - prices[i])
            max_right = max(prices[i], max_right)
        return ans