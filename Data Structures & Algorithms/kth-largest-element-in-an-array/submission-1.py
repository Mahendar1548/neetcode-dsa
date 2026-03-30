class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
        desired_idx = nums_len - k
        start, end = 0, nums_len - 1
        while True:
            pivot = self.partition(nums, start, end)
            if pivot == desired_idx:
                return nums[pivot]
            elif desired_idx > pivot:
                start = pivot + 1
            else:
                end = pivot - 1
        
    def partition(self, nums, start, end):
        pivot = end
        swap_idx = start
        
        for i in range(start, end):
            if nums[i] < nums[pivot]:
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
                swap_idx += 1
        
        nums[swap_idx], nums[pivot] = nums[pivot], nums[swap_idx]
        return swap_idx
