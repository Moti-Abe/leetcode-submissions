# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # traverse through l1 and add all values in list to s1
        s1 = ""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next

        # traverse through l2 and add all values in list to s2
        s2 = ""
        while l2:
            s2 += str(l2.val)
            l2 = l2.next

        # reverse s1 and s2
        s1 = s1[::-1]
        s2 = s2[::-1]

        # change s1 and s2 to int
        n1 = int(s1)
        n2 = int(s2)

        # find their sum
        total = n1 + n2

        # convert sum to string
        s = str(total)

        # reverse sum string
        s = s[::-1]

        # convert reversed sum string to output list (linked list)
        dummy = ListNode(0)
        curr = dummy

        for ch in s:
            curr.next = ListNode(int(ch))
            curr = curr.next

        return dummy.next