class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # print("mahi")
        idx_wise_value = {idx: val for idx, val in enumerate(queries)}
        queries.sort()
        # print("hello")

        min_heap = []
        for each in intervals:
            min_heap.append((each[1] - each[0] + 1, each))

        heapq.heapify(min_heap)
        val_wise_ans = dict()

        while min_heap:
            val, ran = heapq.heappop(min_heap)

            pivot = self._get_pivot_idx(queries, ran[0])
            print(queries, pivot)
            while pivot < len(queries) and queries[pivot] <= ran[1]:
                if queries[pivot] in val_wise_ans or not ran[0] <= queries[pivot] <= ran[1]:
                    pivot += 1
                    continue
                else:
                    val_wise_ans[queries[pivot]] = val
                    pivot += 1

        return [
            val_wise_ans.get(idx_wise_value[i], -1)
            for i in range(len(queries))
        ]

    def _get_pivot_idx(self, data, val):
        low = 0
        high = len(data) - 1

        while low < high:
            mid = (low + high) // 2
            if data[mid] > val:
                high = mid - 1
            elif data[mid] < val:
                low = mid + 1
            else:
                high = mid

        return low