class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_wise_adj = defaultdict(list)
        for src, dest in edges:
            node_wise_adj[src].append(dest)
            node_wise_adj[dest].append(src)

        visited = set()
        def dfs(node, prev_node):
            if node in visited:
                return False

            visited.add(node)
            for adj_node in node_wise_adj[node]:
                if adj_node == prev_node:
                    continue
                if not dfs(adj_node, node):
                    return False

            return True

        
        return n == len(visited) if dfs(0, -1) else False