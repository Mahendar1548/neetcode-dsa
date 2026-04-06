class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        cache = dict()
        stack = [root]

        while stack:
            curr_node = stack[-1]
            left, right = curr_node.left, curr_node.right
            if right and right not in cache:
                stack.append(right)
            elif left and left not in cache:
                stack.append(left)
            else:
                node_to_process = stack.pop()
                self._set_node(node_to_process, cache)

        return max(cache[root])

    def _set_node(self, node, cache):
        left_value = self._get_cache_value(node.left, cache) if node else [0,0]
        right_value = self._get_cache_value(node.right, cache) if node else [0,0]

        including = left_value[1] + right_value[1] + node.val
        excluding = left_value[0] + right_value[0]

        cache[node] = [max(including, excluding), left_value[0]+right_value[0]]


    def _get_cache_value(self, node, cache):
        if node not in cache:
            cache[node] = [0, 0]

        return cache[node]
