

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None and head.next == None:
            return head
        
        curr = head
        arr = []
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        
        reversed_arr = arr[::-1]
        print(arr)
        print(reversed_arr)
        l, r = 0, 0
        dummy = ListNode(-1)
        temp = dummy
        while l < len(arr)//2:
            node1 = ListNode(arr[l])
            temp.next = node1
            temp = temp.next
            node2 = ListNode(reversed_arr[r])
            temp.next = node2
            temp = temp.next
            l += 1
            r += 1

        if len(arr)%2 != 0:
            temp.next = ListNode(arr[l])
        head.next = dummy.next.next
        return head

        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna