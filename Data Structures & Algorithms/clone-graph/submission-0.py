"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        new_map = dict()
        visited = set()

        q = deque()
        q.append(node)
        new_map[node.val] = Node(node.val)

        while q:
            curr_node = q.popleft()
            visited.add(curr_node.val)

            for neigh in curr_node.neighbors:
                if neigh.val not in new_map:
                    new_map[neigh.val] = Node(neigh.val)
                new_map[curr_node.val].neighbors.append(new_map[neigh.val])
                if neigh.val not in visited:
                    q.append(neigh)

        return new_map[node.val]
