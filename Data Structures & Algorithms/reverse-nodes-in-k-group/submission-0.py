class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_start = dummy
        curr_start = head
        ll_len = 0
        temp = head
        while temp:
            ll_len += 1
            temp = temp.next

        for i in range(ll_len // k):
            temp = curr_start
            prev = None
            for j in range(k):
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            prev_start.next = prev
            prev_start = curr_start
            curr_start = temp
        prev_start.next = curr_start

        return dummy.next
