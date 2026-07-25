class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid (root, left, right):
            if not root:
                return True
            
            if not((root.val < right) and (root.val > left)):
                return False
            
            return (valid(root.left, left, root.val) and
                    valid(root.right,root.val, right))
        
        return valid(root, float(-inf), float(inf))



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna