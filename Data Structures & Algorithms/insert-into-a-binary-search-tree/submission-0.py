class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val=val)
        if not root:
            return new_node
        
        def dfs(node):
            if node.val < val:
                if not node.right:
                    node.right = new_node
                else:
                    dfs(node.right)
            else:
                if not node.left:
                    node.left = new_node
                else:
                    dfs(node.left)
        
        dfs(root)
        return root
