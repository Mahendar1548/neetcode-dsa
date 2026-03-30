import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        heap_data = []
        for key, value in freq.items():
            heap_data.append((-value, key))

        heapq.heapify(heap_data)
        q = deque()

        count = 0
        latest_popped = heapq.heappop(heap_data) if heap_data else None
        while latest_popped:
            count += 1
            if latest_popped[0] != -1:
                q.append((count+n, latest_popped[0] + 1, latest_popped[1]))
    
            if (q and q[0][0] == count) or (not heap_data and q):
                data = q.popleft()
                count = data[0]
                heapq.heappush(heap_data, (data[1], data[2]))

            latest_popped = heapq.heappop(heap_data) if heap_data else None
        return count