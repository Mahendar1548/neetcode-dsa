class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last = intervals[0]
        ans = 0

        for each in intervals[1:]:
            if last[1] > each[0]:
                ans += 1
            else:
                last = each
        
        return ans
        