class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(each[0], each[1], idx) for idx, each in enumerate(tasks, 0)]
        tasks.sort()
        
        min_heap = []
        curr_time = 0
        i = 0
        ans = []
        while i < len(tasks):
            if tasks[i][0] <= curr_time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2], tasks[i][0]))
                i += 1
                continue
            if not min_heap:
                curr_time = tasks[i][0]
                continue

            curr_proc = heapq.heappop(min_heap)
            ans.append(curr_proc[1])
            curr_time += curr_proc[0]

        while min_heap:
            curr_proc = heapq.heappop(min_heap)
            ans.append(curr_proc[1])

        return ans