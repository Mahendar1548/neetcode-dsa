class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_till_now = float("-inf")
        total = 1
        curr_max = 1
        curr_min = 1
        for value in nums:
            total *= value
            curr_max *= value
            curr_min *= value
            curr_max = max(curr_max, value)
            curr_min = min(curr_min, value)
            if curr_min > curr_max:
                curr_min, curr_max = curr_max, curr_min
            max_till_now = max(max_till_now, curr_max, total)
        
        return max(max_till_now, total)
        