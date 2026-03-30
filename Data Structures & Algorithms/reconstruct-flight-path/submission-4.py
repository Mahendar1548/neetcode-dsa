class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        node_wise_adj = defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            node_wise_adj[src].append(dst)

        ans = []
        def dfs(station):
            print(station)
            adj_nodes = list(node_wise_adj[station])
            while adj_nodes:
                next_station = adj_nodes.pop(0)
                node_wise_adj[station] = list(adj_nodes)
                dfs(next_station)
                adj_nodes = list(node_wise_adj[station])
            
            ans.append(station)

        dfs("JFK")
        ans.reverse()
        return ans
