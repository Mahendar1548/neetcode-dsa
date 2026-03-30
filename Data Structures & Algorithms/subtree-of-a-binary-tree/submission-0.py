# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root:
            return self._is_same_subtree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False

    def _is_same_subtree(self, p, q):
        if not p and not q:
            return True

        if p and q and q.val == p.val:
            return self._is_same_subtree(p.left, q.left) and self._is_same_subtree(p.right, q.right)
        return False
