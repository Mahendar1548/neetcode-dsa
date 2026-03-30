class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        left = dummy_node
        right = head
        
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        
        return dummy_node.next