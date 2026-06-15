# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(crtnode, leftval, rightval):
            if not crtnode:
                return True
            
            if not leftval < crtnode.val < rightval:
                return False

            return isValid(crtnode.left, leftval, crtnode.val) and isValid(crtnode.right, crtnode.val, rightval)

        return isValid(root, float("-inf"), float("inf"))