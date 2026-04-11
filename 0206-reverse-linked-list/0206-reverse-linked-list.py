# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        if head == None:
            return head
        
        while head:
            new_node = ListNode(head.val)
            if dummy == None:
                dummy = new_node
            else:
                new_node.next = dummy
                dummy = new_node
            head = head.next
        
        return dummy
        
