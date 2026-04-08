class Solution:
    def reorganizeString(self, s: str) -> str:
        char_wise_count = Counter(s)
        min_heap = [(-value, key) for key, value in char_wise_count.items()]
        heapq.heapify(min_heap)

        ans = []
        curr_item = heapq.heappop(min_heap)
        ans.append(curr_item[1])
        while min_heap:
            tmp = heapq.heappop(min_heap)
            if curr_item[0] != -1:
                heapq.heappush(min_heap, (curr_item[0]+1, curr_item[1]))
            curr_item = tmp
            ans.append(curr_item[1])

        if curr_item[0] < -1:
            return ""

        return "".join(ans)