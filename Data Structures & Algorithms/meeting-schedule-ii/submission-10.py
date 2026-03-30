class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        min_heap = []

        ans = 0
        for interval in intervals:
            while min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            ans = max(ans, len(min_heap))

        return ans