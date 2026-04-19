class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # count nodes
        n = 0
        dummy = ListNode(0)
        dummy.next = head
        left = head 
        while left:
            n += 1
            left = left.next

        k = k % n
        if k == 0:
            return head

        count = 0
        tail = None

        while count < (n - k):
            count += 1
            if count == (n - k):
                tail = head
            head = head.next

        # break
        tail.next = None
        res = head

        # go to end of second part
        while head.next:
            head = head.next

        # connect
        head.next = dummy.next

        return res