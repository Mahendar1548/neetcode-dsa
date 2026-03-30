class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        return max(nums[0] + self._max_rob(nums[2:nums_len-1]),
                   nums[1] + self._max_rob(nums[3:]))

    def _max_rob(self, nums):
        rob1 = rob2 = 0
        for value in nums:
            temp = max(rob1+value, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
