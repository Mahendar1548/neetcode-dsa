# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        
        if list2 and not list1:
            return list2
        
        if not list1 and not list2:
            return list1
        
        if list2.val < list1.val:
            list1, list2 = list2, list1
        
        l1p, l2p = list1, list2
        l1p_prev = None
        
        while l1p and l2p:
            if l1p.val <= l2p.val:
                l1p_prev = l1p
                l1p = l1p.next
            else:
                temp = l2p
                l2p = l2p.next
                l1p_prev.next = temp
                temp.next = l1p
                l1p_prev = temp
        if l2p:
            l1p_prev.next = l2p
        
        return list1
