# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        ll_len = 0
        temp = head
        
        while temp:
            ll_len += 1
            temp = temp.next
        
        index_to_removed = ll_len - n
        if index_to_removed == 0:
            return head.next
        
        prev = None
        curr = head
        
        curr_count = 0
        while curr_count != index_to_removed:
            prev = curr
            curr = curr.next
            curr_count += 1
        
        prev.next = curr.next
        
        return head