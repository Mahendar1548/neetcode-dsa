class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current_ptr = 0
        for i in range(1, len(nums)):
            if nums[current_ptr] != nums[i]:
                current_ptr += 1
                nums[current_ptr] = nums[i]
        
        return current_ptr + 1