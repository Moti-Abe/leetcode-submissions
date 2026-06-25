# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head 
        while curr:
            arr.append(curr.val)
            curr = curr.next
        reversed_arr = arr[::-1]

        curr = head
        i = 0
        while curr and i < len(arr)//2:
            curr.val = arr[i]
            curr = curr.next
            curr.val = reversed_arr[i]
            curr = curr.next  
            i += 1
        if curr:
            curr.val = arr[i]
        print(arr)
        print(reversed_arr)
        return head  

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna