class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # dummy heads
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        
        # pointers to build lists
        smaller = smaller_head
        greater = greater_head
        
        # traverse original list
        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        
        # VERY IMPORTANT: avoid cycle
        greater.next = None
        
        # connect lists
        smaller.next = greater_head.next
        
        return smaller_head.next