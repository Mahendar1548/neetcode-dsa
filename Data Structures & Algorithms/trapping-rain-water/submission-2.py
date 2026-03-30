class Solution:
    def trap(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        max_left, max_right = height[0], height[-1]
        
        ans = 0
        while lp < rp:
            comm_height = min(max_left, max_right)
            if height[lp] <= height[rp]:
                curr_height = height[lp]
                lp += 1
                max_left = max(max_left, curr_height)
            else:
                curr_height = height[lp]
                rp -= 1
                max_right = max(max_right, curr_height)
            
            ans += comm_height - curr_height if comm_height - curr_height > 0 else 0
        
        return ans
