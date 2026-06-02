# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We traverse the tree using a while loop.
We steer directions as we go along
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        crt = root

        while crt:
            if p.val < crt.val and q.val < crt.val:
                crt = crt.left
                continue
            if p.val > crt.val and q.val > crt.val:
                crt = crt.right
                continue

            return crt