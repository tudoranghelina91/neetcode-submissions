# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        result = []

        if not root:
            return []

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                crt = q.popleft()
                level.append(crt.val)
                if crt.left:
                    q.append(crt.left)
                
                if crt.right:
                    q.append(crt.right)
            
            if level:
                result.append(level)

        return result