class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque()
        if root:
            q.append(root)

        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == q_len - 1:
                    ans.append(node.val)
                

        return ans
