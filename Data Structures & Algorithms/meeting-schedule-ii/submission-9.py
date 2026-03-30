class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        min_heap = []

        i = 0
        ans = 0
        while i < len(intervals):
            while min_heap and min_heap[0] <= intervals[i].start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, intervals[i].end)
            ans = max(ans, len(min_heap))
            i += 1
        
        return ans