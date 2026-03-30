class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_value = 0
        nl = len(heights)
        lp = 0
        rp = nl - 1

        while lp < rp:
            max_value = max(max_value, min(heights[lp], heights[rp]) * (rp - lp))
            if heights[rp] < heights[lp]:
                rp -= 1
            else:
                lp += 1

        return max_value