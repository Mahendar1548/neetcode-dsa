"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.end)
        lastVal = intervals[0].end
        for idx in range(1, len(intervals)):
            if lastVal > intervals[idx].start:
                return False
            lastVal = intervals[idx].end
        
        return True

