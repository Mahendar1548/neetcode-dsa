class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_till_now = float("-inf")
        def dfs(node):
            nonlocal max_till_now
            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            max_till_now = max(
                max_till_now, left_max, right_max, left_max + right_max + node.val)

            return max(left_max + node.val, right_max + node.val, node.val)

        dfs(node=root)
        return max_till_now