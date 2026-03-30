# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def count_good_nodes(node, max_till_here):
            nonlocal count
            if not node:
                return 
            if node.val >= max_till_here:
                count += 1
                max_till_here = node.val
            
            count_good_nodes(node.left, max_till_here)
            count_good_nodes(node.right, max_till_here)
        
        count_good_nodes(root, - float("inf"))
    
        return count
