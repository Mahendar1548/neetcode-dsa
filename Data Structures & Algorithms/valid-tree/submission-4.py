class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_wise_neighbours = defaultdict(list)
        for x, y in edges:
            node_wise_neighbours[x].append(y)

        visited = set()
        def dfs(node):
            print(node)
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in node_wise_neighbours[node]:
                if not dfs(neigh):
                    return False
            return True
        
        ans = True
        for node in list(node_wise_neighbours.keys()):
            if node not in visited:
                ans = ans and dfs(node)

        return ans and len(visited) == n