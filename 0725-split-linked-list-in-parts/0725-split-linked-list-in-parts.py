class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: count length
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        # Step 2: base size and extra nodes
        size = n // k
        extra = n % k
        
        result = []
        curr = head
        
        # Step 3: split
        for i in range(k):
            part_head = curr
            part_size = size + (1 if i < extra else 0)
            
            # move to end of this part
            for j in range(part_size - 1):
                if curr:
                    curr = curr.next
            
            # cut the list
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            result.append(part_head)
        
        return result