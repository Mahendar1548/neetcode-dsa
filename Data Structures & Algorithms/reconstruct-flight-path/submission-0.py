class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        node_wise_adj = defaultdict(list)

        for src, dst in tickets:
            node_wise_adj[src].append(dst)
        for node, adjs in node_wise_adj.items():
            adjs.sort()

        ans = []
        def dfs(station):
            ans.append(station)
            # print(ans)

            for i in range(len(node_wise_adj[station])):
                next_station = node_wise_adj[station].pop(i)
                dfs(next_station)
                if len(ans) != len(tickets)+1:
                    node_wise_adj[station].insert(i, next_station)
                else:
                    break
            if len(ans) != len(tickets)+1:
                ans.pop()

        dfs("JFK")
        return ans