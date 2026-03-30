class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = - float("inf")
        max_sum_from_here = 0

        for num in nums:
            max_sum_from_here = max(max_sum_from_here + num, num)
            max_sum = max(max_sum, max_sum_from_here)
        
        return max_sum