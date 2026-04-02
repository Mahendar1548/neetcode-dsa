class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key == root.val:
            if root.left and root.right:
                root.left = self._insertIntoBST(root.left, root.right)
                return root.left
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return root.left
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        
        return root

    def _insertIntoBST(self, root: Optional[TreeNode], node: TreeNode) -> Optional[TreeNode]:
        if not root:
            return node
        elif root.val < node.val:
            root.right = self._insertIntoBST(root.right, node)
        else:
            root.left = self._insertIntoBST(root.left,node)
        return root