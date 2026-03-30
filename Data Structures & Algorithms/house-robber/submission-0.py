class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(2, n):
            prev_rob_aggr = nums[i-2]
            if i-3 >= 0:
                prev_rob_aggr = max(prev_rob_aggr, nums[i-3])
            nums[i] += prev_rob_aggr
        
        return max(nums[n-1], nums[n-2]) if n > 1 else nums[n-1]
        