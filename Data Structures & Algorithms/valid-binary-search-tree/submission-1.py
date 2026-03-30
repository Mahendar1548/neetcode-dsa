class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_bst(node, max_till_now, is_left):
            if not node:
                return True

            if (is_left and node.val < max_till_now) or (not is_left and node.val > max_till_now):
                return is_bst(node.left, node.val, True) and is_bst(node.right, max(max_till_now, node.val), False)
            else:
                return False

        return is_bst(root, float("-inf"), False)
