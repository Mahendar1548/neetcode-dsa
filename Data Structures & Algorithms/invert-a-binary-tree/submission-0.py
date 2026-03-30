class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._invert(root)
        return root

    def _invert(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self._invert(node.left)
        self._invert(node.right)
