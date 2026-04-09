class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        curr_char = None
        curr_char_count = 0
        ans = []
        max_heap = []
        if a:
            max_heap.append((-a, "a"))
        if b:
            max_heap.append((-b, "b"))
        if c:
            max_heap.append((-c, "c"))

        heapq.heapify(max_heap)
        curr_item = None

        while max_heap:
            count, char = heapq.heappop(max_heap)
            ans.append(char)
            if char == curr_char:
                curr_char_count += 1
            else:
                curr_char = char
                curr_char_count = 1

            if curr_char_count == 2 and count < -1:
                curr_item = (count, char)

            if curr_char_count == 1:
                if count < -1:
                    heapq.heappush(max_heap, (count + 1, char))
                if curr_item:
                    heapq.heappush(max_heap, (curr_item[0]+1, curr_item[1]))
                    curr_item = None

        return "".join(ans)