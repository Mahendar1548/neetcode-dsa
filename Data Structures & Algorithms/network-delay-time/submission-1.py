class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node_wise_adj = defaultdict(list)
        for src, dst, distance in times:
            node_wise_adj[src].append([distance, dst])

        visited = set()
        max_value = float("-inf")

        min_heap = [[0, k]]
        while min_heap and len(visited) < n:
            distance, node = heapq.heappop(min_heap)
            if node in visited:
                continue

            visited.add(node)
            max_value = max(max_value, distance)
            for dis, dst in node_wise_adj[node]:
                if dst not in visited:
                    heapq.heappush(min_heap, [dis+distance, dst])

        return max_value if len(visited) == n else -1
