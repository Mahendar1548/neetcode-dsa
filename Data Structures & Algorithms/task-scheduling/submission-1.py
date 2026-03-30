import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        letter_wise_last_exec_time = dict()

        heap_data = []
        for key, value in freq.items():
            heap_data.append((1, -value, key))

        heapq.heapify(heap_data)
        print(heap_data)
        count = 0
        latest_popped = heapq.heappop(heap_data) if heap_data else None
        while latest_popped:
            print(letter_wise_last_exec_time)
            print(heap_data)
            count += 1
            last_exec_time = letter_wise_last_exec_time.get(latest_popped[2])
            if last_exec_time and last_exec_time + n + 1 > count:
                count = last_exec_time + n + 1
            letter_wise_last_exec_time[latest_popped[2]] = count
            if latest_popped[1] != -1:
                heapq.heappush(heap_data, (count + n+1, latest_popped[1] + 1, latest_popped[2]))

            latest_popped = heapq.heappop(heap_data) if heap_data else None

        return count