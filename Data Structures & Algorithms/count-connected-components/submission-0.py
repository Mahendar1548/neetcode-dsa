class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_wise_adj = defaultdict(list)
        for src, dst in edges:
            node_wise_adj[src].append(dst)
            node_wise_adj[dst].append(src)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for adj in node_wise_adj[node]:
                if adj not in visited:
                    dfs(adj)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
                
        
        return ans