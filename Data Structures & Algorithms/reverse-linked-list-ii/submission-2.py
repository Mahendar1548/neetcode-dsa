class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        prev = None
        current = head
        i = 1
        while i < left:
            prev = current
            current = current.next
            i += 1
        first_break = prev
        joint_last = current

        prev = None
        current = current
        while i <= right:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i += 1
        
        if first_break is None:
            head = prev
        else:
            first_break.next = prev
        
        if current is not None:
            joint_last.next = current
        
        return head
        