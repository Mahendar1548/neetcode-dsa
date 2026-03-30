# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        nodes_len = len(preorder)
        root = TreeNode(val=preorder[0])
        stack = [root]
        pre_ptr = 1
        in_ptr = 0
        curr_node = None
        
        while in_ptr < nodes_len:
            if stack and stack[-1].val == inorder[in_ptr]:
                curr_node = stack.pop()
                in_ptr += 1
            elif curr_node and (not stack or (stack[-1].val != inorder[in_ptr])):
                new_node = TreeNode(val=preorder[pre_ptr])
                curr_node.right = new_node
                stack.append(new_node)
                pre_ptr += 1
                curr_node = None
            elif not curr_node and stack and stack[-1].val != inorder[in_ptr]:
                new_node = TreeNode(val=preorder[pre_ptr])
                stack[-1].left = new_node
                stack.append(new_node)
                pre_ptr += 1
                curr_node = None
            
        return root