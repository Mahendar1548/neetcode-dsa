class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, left, right):
            if not node:
                return True
            
            if left < node.val < right:
                return is_valid(node.left, left, node.val) and is_valid(node.right, node.val, right)
            
            return False
            

        return is_valid(root, float("-inf"), float("inf"))
