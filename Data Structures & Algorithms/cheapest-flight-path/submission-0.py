class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        char_wise_adj_data = {i:[] for i in range(n)}

        for src_, dst_, cost in flights:
            char_wise_adj_data[src_].append((dst_, cost))

        visited = set()
        min_heap = [(0, src, 0)]

        while min_heap:
            print(min_heap, src, dst)
            agg_cost, station, stops = heapq.heappop(min_heap)
            if station in visited:
                continue
                
            if station == dst:
                print("Hi")
                return agg_cost
            
            if stops > k:
                continue

            visited.add(station)
            print(visited)
            for neigh, cost in char_wise_adj_data[station]:
                if neigh in visited:
                    continue
                heapq.heappush(min_heap, (agg_cost+cost, neigh, stops + 1))

        return -1
