class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_till_now = float("-inf")
        total = 1
        curr = 1
        for value in nums:
            total *= value
            curr *= value
            curr = max(curr, value)
            max_till_now = max(max_till_now, curr, total)
        
        return max(max_till_now, total)
        