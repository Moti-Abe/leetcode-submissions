class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        fast = slow = dummy
        
        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove the target node
        slow.next = slow.next.next
        
        return dummy.next