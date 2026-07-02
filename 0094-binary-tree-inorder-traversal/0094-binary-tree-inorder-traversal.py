# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Perform inorder traversal (left -> node -> right) using recursion.
        output = []
        def inorder(root):
            if not root: return output  # Base case: reached a null node; recursion stops.
        
            inorder(root.left)  # Recurse on left subtree.
            output.append(root.val)  # Visit current node.
            inorder(root.right)  # Recurse on right subtree.
        inorder(root)
        # Time Complexity: O(N) where N is the number of nodes.
        # Space Complexity: O(N) for output list + O(H) recursion stack (H = tree height, worst-case O(N)).
        return output

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna