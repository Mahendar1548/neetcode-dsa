class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        q = deque()
        q.append(root)
        data = []

        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if not node:
                    continue
                val = f"{node.val}|{node.left.val if node.left else 'N'}|{node.right.val if node.right else 'N'}"
                data.append(val)
                q.append(node.left)
                q.append(node.right)

        return "#".join(data)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        node_wise_data = {None:None}
        data_chunks = data.split("#")
        
        for each in data_chunks:
            node, left, right = each.split("|")
            node_val, left_val, right_val = int(node), int(left) if left != 'N' else None, int(right) if right != 'N' else None
            if node_val not in node_wise_data:
                node_wise_data[node_val] = TreeNode(val=node_val)
            if left_val not in node_wise_data:
                node_wise_data[left_val] = TreeNode(val=left_val)
            if right_val not in node_wise_data:
                node_wise_data[right_val] = TreeNode(val=right_val)
            node_wise_data[node_val].left = node_wise_data[left_val]
            node_wise_data[node_val].right = node_wise_data[right_val]
        
        return node_wise_data[int(data.split("|")[0])]
