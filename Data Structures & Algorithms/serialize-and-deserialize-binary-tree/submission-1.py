class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return 
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print("Data", ",".join(res))
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        def dfs():
            print(self.i)
            if values[self.i] == "N":
                self.i += 1
                return None
            
            new_node = TreeNode(val=int(values[self.i]))
            self.i += 1
            new_node.left = dfs()
            new_node.right = dfs()
            
            return new_node
        
        return dfs()
        