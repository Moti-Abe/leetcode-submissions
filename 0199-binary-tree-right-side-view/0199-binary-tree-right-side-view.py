# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            ans = []
            if not root:
                return ans
            q = deque()
            q.append(root)

            while q:
                size = len(q)
                ans.append(q[-1].val)
                
                for i in range(size):
                    node = q.popleft()

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            return ans
        return bfs(root)

        
                    



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna