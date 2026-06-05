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
            if crt.val < p.val and crt.val < q.val:
                crt = crt.right
                continue
            if crt.val > p.val and crt.val > q.val:
                crt = crt.left
                continue

            return crt