"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.end)

        ans = 1
        curr_ans = 1
        last_end = intervals[0].end
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr.start < last_end:
                curr_ans += 1
            else:
                curr_ans = 1
            ans = max(ans, curr_ans)
            last_end = curr.end
        
        return ans

        