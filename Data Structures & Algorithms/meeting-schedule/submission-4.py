class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        max_start = None
        val_wise_freq = defaultdict(int)
        for interval in intervals:
            val_wise_freq[interval.start] += 1
            val_wise_freq[interval.end] -= 1
            if max_start is None:
                max_start = interval.start
            max_start = max(max_start, interval.start)
        
        curr_value = 0
        for i in range(max_start+1):
            curr_value += val_wise_freq[i]
            if curr_value > 1:
                return False
        
        return True