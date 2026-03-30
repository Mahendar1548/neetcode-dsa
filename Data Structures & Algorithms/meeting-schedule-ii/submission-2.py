"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        data = defaultdict(int)
        for each in intervals:
            data[each.start] += 1
            data[each.end] -= 1
        
        ans = -float("inf")
        curr = 0
        for val in sorted(data):
            curr += data[val]
            ans = max(ans, curr)
        
        return ans

        