class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        ans = float("inf")
        
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                if curr_sum >= target:
                    ans = min(ans, (i - start) + 1)
                
                curr_sum -= nums[start]
                start += 1
        
        return 0 if ans == float("inf") else ans