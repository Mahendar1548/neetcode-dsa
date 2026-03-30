class FindUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        node1_repr = self.find(node1)
        node2_repr = self.find(node2)
        
        if node1_repr == node2_repr:
            return 
        
        if self.rank[node1_repr] > self.rank[node2_repr]:
            self.parent[node2_repr] = node1_repr
        elif self.rank[node2_repr] > self.rank[node1_repr]:
            self.parent[node1_repr] = node2_repr
        else:
            self.parent[node1_repr] = node2_repr
            self.rank[node2_repr] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        find_union = FindUnion(n)
        for src, dst in edges:
            find_union.union(src, dst)
        
        parents = set()
        for i in range(n):
            parents.add(find_union.find(i))
        
        return len(parents)