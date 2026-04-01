class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        visit = [False]
        ans = []

        while stack:
            node, is_visited = stack.pop(), visit.pop()
            if node:
                if is_visited:
                    ans.append(node.val)
                else:
                    stack.append(node.right)
                    visit.append(False)
                    stack.append(node)
                    visit.append(True)
                    stack.append(node.left)
                    visit.append(False)
        
        return ans