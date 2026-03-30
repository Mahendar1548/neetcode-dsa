class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n > 1 and len(edges)==0:
            return False
        node_wise_neighbours = defaultdict(list)
        for x, y in edges:
            if y in node_wise_neighbours:
                x, y = y, x
            node_wise_neighbours[x].append(y)

        visited = set()
        def dfs(node):
            # print(node)
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in node_wise_neighbours[node]:
                if not dfs(neigh):
                    return False
            return True


        return dfs(edges[0][0]) and len(visited) == n