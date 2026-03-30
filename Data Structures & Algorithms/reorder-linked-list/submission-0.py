class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        global ll_len
        if not head:
            return head

        globals()["ll_len"] = 0
        temp = head
        while temp:
            ll_len += 1
            temp = temp.next

        globals()["half"] = ll_len // 2
        globals()["temp_start"] = head

        def reorder(second):
            global half, temp_start
            if not second:
                return
            reorder(second.next)
            if half:
                half -= 1
                inter = temp_start.next
                temp_start.next = second
                if half:
                    second.next = inter
                    temp_start = inter
                if not half:
                    if ll_len % 2:
                        second.next = inter
                        inter.next = None
                    else:
                        second.next = None

        reorder(head)