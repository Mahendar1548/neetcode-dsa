# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l1p, l2p = l1, l2
        result = result_head = ListNode(0)
        
        while l1p and l2p:
            value = l1p.val + l2p.val + carry
            result.next = ListNode(val=value%10)
            result = result.next
            carry = value // 10
            l1p, l2p = l1p.next, l2p.next
        
        left = l1p or l2p
        while left:
            value = left.val + carry
            result.next = ListNode(val=value % 10)
            result = result.next
            carry = value // 10
            left = left.next
        
        if carry:
            result.next = ListNode(val=carry)
        
        return result_head.next
