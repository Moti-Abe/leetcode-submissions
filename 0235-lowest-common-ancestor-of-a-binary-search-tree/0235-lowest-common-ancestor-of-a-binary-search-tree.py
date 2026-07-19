# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if not root:
                return None
            
            if p.val <= root.val <= q.val:
                return root
            
            if p.val > root.val and q.val > root.val:
                return helper(root.right, p, q)
            
            elif p.val < root.val and q.val < root.val:
                return helper(root.left, p, q)
            else:
                return root
        
        return helper(root, p, q)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna