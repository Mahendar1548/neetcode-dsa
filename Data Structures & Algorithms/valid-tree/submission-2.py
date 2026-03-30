class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_wise_adj = defaultdict(list)
        for src, dest in edges:
            if src == dest:
                return False
            node_wise_adj[src].append(dest)
            node_wise_adj[dest].append(src)
            
        visited = set()
        q = deque()
        q.append(0)
        visited.add(0)
        
        while q:
            node = q.popleft()
            for adj_node in list(node_wise_adj[node]):
                if adj_node == node:
                    continue
                if adj_node in visited:
                    return False
                q.append(adj_node)
                visited.add(adj_node)
                node_wise_adj[adj_node].remove(node)
        
        return n == len(visited)
