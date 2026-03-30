class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        idx_wise_value = {idx: val for idx, val in enumerate(queries)}
        queries_set = set(queries)

        min_heap = []
        for each in intervals:
            min_heap.append((each[1]-each[0]+1, each))
        
        heapq.heapify(min_heap)
        val_wise_ans = dict()
        idx = 0
        while min_heap:
            val, ran = heapq.heappop(min_heap)
            for i in range(ran[0], ran[1]+1):
                if i in val_wise_ans:
                    continue
                else:
                    val_wise_ans[i] = val
        
        return [
            val_wise_ans.get(idx_wise_value[i], -1)
            for i in range(len(queries))
        ]
        
