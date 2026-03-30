class Solution:
    def trap(self, height: List[int]) -> int:
        height_len = len(height)
        max_from_left = [0] * height_len
        max_from_right = [0] * height_len

        for i in range(1, height_len):
            max_from_left[i] = max(max_from_left[i-1], height[i-1])
            max_from_right[height_len-1-i] = max(max_from_right[height_len-i], height[height_len-i])

        max_trap = 0
        for i in range(height_len):
            value_to_add = min(max_from_left[i], max_from_right[i]) - height[i]
            max_trap += value_to_add if value_to_add > 0 else 0
        return max_trap
