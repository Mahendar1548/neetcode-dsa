class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            is_possible = self._is_possible(nums, k, mid)
            if is_possible:
                high = mid
            else:
                low = mid + 1
        
        return high
    
    
    def _is_possible(self, nums: List[int], k, target) -> bool:
        batches = 1
        curr_batch = 0
        for num in nums:
            if curr_batch + num <= target:
                curr_batch += num
            else:
                batches += 1
                curr_batch = num
        
        return batches <= k