class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        nums_set = set(nums)
        for value in nums_set:
            if value - 1 in nums_set:
                continue
            current_count = 1
            while value + 1 in nums_set:
                current_count += 1
                value += 1
            max_count = max(max_count, current_count)
        
        return max_count
