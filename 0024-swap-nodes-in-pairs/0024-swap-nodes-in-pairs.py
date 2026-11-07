# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        res_dummy = dummy
        if not head or head.next == None:
            return head

        while head and head.next:
            next_pair = head.next.next
            
            dummy.next = head.next
            dummy = dummy.next

            dummy.next = head
            dummy = dummy.next

            head = next_pair
        dummy.next = head
        return res_dummy.next