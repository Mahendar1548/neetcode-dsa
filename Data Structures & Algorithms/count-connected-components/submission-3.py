class DisJointSet:
    def __init__(self, n):
        self.comps = n
        self.parents = {i:i for i in range(n)}
        self.size = {i: 1 for i in range(n)}
    
    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        
        if x_parent == y_parent:
            return
        
        self.comps -= 1
        
        if self.size[x_parent] < self.size[y_parent]:
            x_parent, y_parent = y_parent, x_parent
        
        self.size[x_parent] += self.size[y_parent]
        self.parents[y_parent] = x_parent
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dj = DisJointSet(n=n)
        
        for a, b in edges:
            dj.union(a, b)
        
        return dj.comps