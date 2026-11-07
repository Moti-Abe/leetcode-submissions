class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def dfs(node):
            curr = node
            last = None
            
            while curr:
                next_node = curr.next
                
                # if child exists
                if curr.child:
                    child_head = curr.child
                    child_tail = dfs(child_head)
                    
                    # connect curr -> child
                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None
                    
                    # connect child tail -> next_node
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail
                    
                    last = child_tail
                    curr = next_node
                else:
                    last = curr
                    curr = next_node
            
            return last
        
        dfs(head)
        return head