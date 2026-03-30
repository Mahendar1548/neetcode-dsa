class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        return max(nums[0] + self._max_rob(nums[2:nums_len-2]),
                   self._max_rob(nums[1:]))

    def _max_rob(self, nums):
        rob1 = rob2 = 0
        for value in nums:
            temp = max(rob1+value, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
