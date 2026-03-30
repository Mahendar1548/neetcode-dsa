class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_till_now = float("-inf")
        def dfs(node):
            nonlocal max_till_now
            if not node:
                return 0

            left_max_for_add = dfs(node.left)
            right_max_for_add = dfs(node.right)


            max_till_now = max(
                max_till_now,
                node.val + left_max_for_add,
                right_max_for_add + node.val,
                left_max_for_add + right_max_for_add + node.val)

            return max(left_max_for_add + node.val, right_max_for_add + node.val, node.val)

        dfs(node=root)
        return max_till_now
