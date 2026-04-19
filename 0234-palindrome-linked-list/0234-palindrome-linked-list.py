# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0)
        curr = head
        while curr:
            new_node = ListNode(curr.val)
            new_node.next = dummy
            dummy = new_node
            curr = curr.next
        
        while head:
            if head.val != dummy.val:
                return False
            head = head.next
            dummy = dummy.next
        return True

