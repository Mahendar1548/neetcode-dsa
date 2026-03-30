"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_wise_new_node = {None: None}
        temp = head
        while temp:
            node_wise_new_node[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            new_node = node_wise_new_node[temp]
            new_node.next = node_wise_new_node[temp.next]
            new_node.random = node_wise_new_node[temp.random]
            temp = temp.next
        
        return node_wise_new_node[head]
