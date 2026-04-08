class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # remove node
            else:
                current = current.next  # move forward
        
        return dummy.next