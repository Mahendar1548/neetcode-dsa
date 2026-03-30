# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque()
        if root:
            q.append(root)
        
        while q:
            node = q.popleft()
            ans.append(node.val)
            if node.right:
                q.append(node.right)
            elif node.left:
                q.append(node.right)
        
        return ans

