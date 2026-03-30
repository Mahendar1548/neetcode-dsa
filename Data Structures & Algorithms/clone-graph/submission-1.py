class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        new_map = dict()
        visited = set()

        q = deque()
        q.append(node)
        visited.add(node.val)
        new_map[node.val] = Node(node.val)

        while q:
            curr_node = q.popleft()
            print(curr_node.val, [each.val for each in curr_node.neighbors])

            for neigh in curr_node.neighbors:
                if neigh.val not in new_map:
                    new_map[neigh.val] = Node(neigh.val)
                new_map[curr_node.val].neighbors.append(new_map[neigh.val])
                if neigh.val not in visited:
                    q.append(neigh)
                    visited.add(neigh.val)
            print(curr_node.val, [each.val for each in new_map[curr_node.val].neighbors])
            print("+++++")

        return new_map[node.val]
