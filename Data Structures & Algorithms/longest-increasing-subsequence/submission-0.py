class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        ans = 0
        for i in range(len(nums)-1, -1, -1):
            max_val = 0
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    max_val = max(max_val, dp[j])
            dp[i] += max_val
            ans = max(ans, dp[i])
        
        return ans


        