class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        node_wise_value = {root: 0}
        while stack:
            top = stack[-1]
            if top is None:
                stack.pop()
                continue
            if node_wise_value[top] == 0:
                if top.left:
                    stack.append(top.left)
                    node_wise_value[top.left] = 0
                node_wise_value[top] += 1
            elif node_wise_value[top] == 1:
                if top.right:
                    stack.append(top.right)
                    node_wise_value[top.right] = 0
                node_wise_value[top] += 1
            elif node_wise_value[top] == 2:
                ans.append(top.val)
                stack.pop()
        
        return ans