class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_left = dummy

        # Step 1: move to node before left
        for _ in range(left - 1):
            prev_left = prev_left.next

        # Step 2: reverse
        curr = prev_left.next
        prev = None

        for _ in range(right - left + 1):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: reconnect
        tail = prev_left.next   # this is original 'left'
        prev_left.next = prev
        tail.next = curr

        return dummy.next