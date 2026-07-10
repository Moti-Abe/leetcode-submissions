class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        root_arr = []
        sub_arr = []

        def postorder(node, arr):
            if not node:
                arr.append("#")
                return

            postorder(node.left, arr)
            postorder(node.right, arr)
            arr.append(node.val)

        postorder(root, root_arr)
        postorder(subRoot, sub_arr)

        m = len(sub_arr)

        for i in range(len(root_arr) - m + 1):
            if root_arr[i:i+m] == sub_arr:
                return True

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna