class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def maxDepth(node):
            nonlocal is_balanced
            if not node:
                return 0
    
            left_max = maxDepth(node.left)
            right_max = maxDepth(node.right)
            is_balanced = is_balanced and abs(left_max-right_max) <= 1
            return 1 + max(left_max, right_max)

        maxDepth(root)
        return is_balanced