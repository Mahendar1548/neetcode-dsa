class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        val_wise_freq = defaultdict(int)
        for interval in intervals:
            val_wise_freq[interval.start] += 1
            val_wise_freq[interval.end] -= 1
        
        val_wise_freq = dict(sorted(val_wise_freq.items(), key=lambda x:x[0]))
        curr = 0
        ans = 0
        for key, value in val_wise_freq.items():
            curr += value
            ans = max(ans, curr)
        
        return ans