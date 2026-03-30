class Solution:
    def trap(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        max_left, max_right = height[lp], height[rp]

        ans = 0
        while lp < rp:
            if height[lp] <= height[rp]:
                lp += 1
                max_left = max(max_left, height[lp])
                ans += max_left - height[lp]
            else:
                rp -= 1
                max_right = max(max_right, height[rp])
                ans += max_right - height[rp]
        return ans
