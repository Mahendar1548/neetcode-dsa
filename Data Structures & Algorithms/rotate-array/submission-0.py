class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return nums

        nums_len = len(nums)
        k = k % nums_len

        nums.reverse()
        self._reverse(nums, 0, k-1)
        self._reverse(nums, k, nums_len-1)
        
    
    def _reverse(self, nums: List[int], start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1