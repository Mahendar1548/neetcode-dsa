# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.maxDepth(root)
        return self.diameter

    def maxDepth(self, node):
        if not node:
            return 0

        left_max = self.maxDepth(node.left)
        right_max = self.maxDepth(node.right)
        self.diameter = max(self.diameter, (left_max + right_max))
        return 1 + max(left_max, right_max)
