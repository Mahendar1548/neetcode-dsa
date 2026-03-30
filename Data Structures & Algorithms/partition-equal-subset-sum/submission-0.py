class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_value = sum(nums)
        if sum_value % 2:
            return False
        
        req_sum = sum_value / 2

        def dfs(idx, curr_sum):
            if req_sum == curr_sum:
                return True
            
            if (curr_sum is not None and req_sum < curr_sum) or idx == len(nums):
                return False
            
            return (dfs(idx+1, curr_sum + nums[idx] if curr_sum is not None else nums[idx]) or dfs(idx+1, curr_sum))
        
        return dfs(0, None)
