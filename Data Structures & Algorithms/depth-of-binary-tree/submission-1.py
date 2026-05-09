# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lsd = 1
        rsd = 1
        maxd = 0
        
        if root.left:
            lsd += self.maxDepth(root.left)
        if root.right:
            rsd += self.maxDepth(root.right)

        maxd = max(maxd, lsd, rsd)
        
        return maxd
