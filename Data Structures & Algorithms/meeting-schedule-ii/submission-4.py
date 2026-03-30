"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.end)

        start = 0
        curr = 1
        ans = 1
        end = 1
        while end < len(intervals):
            if intervals[start].end > intervals[end].start:
                curr += 1
                end += 1
            else:
                curr -= 1
                start += 1
            
            ans = max(ans, curr)
        
        return ans


        for curr in range(1, len(intervals)):
            pass


    # def minMeetingRooms(self, intervals: List[Interval]) -> int:
    #     if not intervals:
    #         return 0
    #     data = defaultdict(int)
    #     for each in intervals:
    #         data[each.start] += 1
    #         data[each.end] -= 1
        
    #     ans = -float("inf")
    #     curr = 0
    #     for val in sorted(data):
    #         curr += data[val]
    #         ans = max(ans, curr)
        
    #     return ans
