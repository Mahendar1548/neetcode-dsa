class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for idx, valu in enumerate(nums, 1):
            total ^= valu
            total ^= idx
        
        return total