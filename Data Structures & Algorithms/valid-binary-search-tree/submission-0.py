# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_bst(node, max_till_now):
            if not node:
                return True
            
            if node.val < max_till_now:
                return is_bst(node.left, node.val) and is_bst(node.right, max(max_till_now, node.val))
            else:
                return False
        
        return is_bst(root, float("inf"))