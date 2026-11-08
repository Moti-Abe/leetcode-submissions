# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        arr = []
        dummy = ListNode(-1)

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()

        curr = dummy
        for num in arr:
            node = ListNode(num)
            curr.next = node
            curr = curr.next

        return dummy.next






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna