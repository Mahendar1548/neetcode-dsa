class FindUnion:
    def __init__(self, n):
        self.parent = [i for i in range(0,n + 1)]
        self.rank = [0] * (n+1)


    def find(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        node1_repr = self.find(node1)
        node2_repr = self.find(node2)

        if node1_repr == node2_repr:
            return True

        if self.rank[node1_repr] > self.rank[node2_repr]:
            self.parent[node2_repr] = node1_repr
        elif self.rank[node2_repr] > self.rank[node1_repr]:
            self.parent[node1_repr] = node2_repr
        else:
            self.parent[node1_repr] = node2_repr
            self.rank[node2_repr] += 1

        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        find_union = FindUnion(n=len(edges))

        ans = None
        for edge in edges:
            is_loop = find_union.union(edge[0], edge[1])
            if is_loop:
                ans = edge

        return ans