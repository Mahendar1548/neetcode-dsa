class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        last = intervals[0]
        ans = 0
        print(intervals)
        for each in intervals[1:]:
            if last[1] > each[0]:
                ans += 1
                # last = each if last[1] > each[1] else last
            else:
                last = each
        
        return ans
        