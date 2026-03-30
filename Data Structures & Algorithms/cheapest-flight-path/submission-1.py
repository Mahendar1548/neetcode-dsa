class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        char_wise_adj_data = {i:[] for i in range(n)}

        for src_, dst_, cost in flights:
            char_wise_adj_data[src_].append((dst_, cost))

        node_to_visited = {src}
        node_wise_min_distance = {i: float("inf") for i in range(n)}
        node_wise_min_distance[src] = 0

        for _ in range(k+1):
            next_to_visited = set()
            node_wise_min_distance_copy = node_wise_min_distance.copy()
            for node in node_to_visited:
                for neigh, cost in char_wise_adj_data[node]:
                    next_to_visited.add(neigh)
                    node_wise_min_distance[neigh] = min(node_wise_min_distance[neigh], cost + node_wise_min_distance_copy[node])
            node_to_visited = next_to_visited
            print(node_wise_min_distance)


        return node_wise_min_distance[dst] if node_wise_min_distance[dst] != float("inf") else -1