class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(node, max_till_here):
            if not node:
                return 0
            
            res = 1 if node.val >= max_till_here else 0
            max_till_here = max(max_till_here, node.val)

            res += count_good_nodes(node.left, max_till_here)
            res += count_good_nodes(node.right, max_till_here)
            return res

        return count_good_nodes(root, root.val)