class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = dict()
    
        def dfs(idx, sum_value):
            if (idx, sum_value) in dp:
                return dp[(idx, sum_value)]
            if idx >= len(nums):
                if target == sum_value:
                    return 1
                return 0
            
            ans = dfs(idx+1, sum_value + nums[idx]) + dfs(idx+1, sum_value - nums[idx])
            dp[(idx, sum_value)] = ans
            
            return ans
        
        return dfs(0, 0)
