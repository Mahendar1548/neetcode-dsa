class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        number_of_jumps = 1
        max_reach = nums[0]
        i = 1
        curr_max = 0
        while True:
            if max_reach >= len(nums) - 1:
                return number_of_jumps
            number_of_jumps += 1
            while i <= max_reach:
                curr_max = max(curr_max, i + nums[i])
                i += 1
            max_reach = curr_max
        