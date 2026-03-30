class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]
        for i in range(1, len(nums)-1):
            max_jump = max(max_jump, i + nums[i])
        
        return max_jump >= len(nums)-1

        