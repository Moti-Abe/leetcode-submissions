# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        q = deque([(root,0)])
        first, last = 0, 0
        while q:
            mmin = q[0][1]
            size = len(q)
            for i in range(size):
                curr_index = q[0][1]-mmin
                node = q[0][0]
                q.popleft()
                if i == 0: first = curr_index
                if i == size-1: last = curr_index
                if node.left: 
                    q.append((node.left, curr_index*2+1))
                if node.right:
                    q.append((node.right, curr_index*2+2))
            ans = max(ans, last-first+1)
        return ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna