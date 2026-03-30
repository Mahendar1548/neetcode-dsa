class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_start = 0
        current = 0
        two_start = len(nums)
        
        while current < two_start:
            if nums[current] == 0:
                nums[zero_start], nums[current] = nums[current], nums[zero_start]
                zero_start += 1
                current += 1
            elif nums[current] == 2:
                nums[two_start-1], nums[current] = nums[current], nums[two_start-1]
                two_start -= 1
            else:
                current += 1