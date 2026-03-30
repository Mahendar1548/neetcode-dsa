class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] <= 0:
                nums[i] = nums_len + 2
        
        for i in range(nums_len):
            curr_value = nums[i]
            while 1 <= curr_value <= nums_len:
                temp_value = nums[curr_value-1]
                nums[curr_value-1] = -1
                curr_value = temp_value
        
        for i in range(nums_len):
            if nums[i] != -1:
                return i + 1
        
        return nums_len + 1