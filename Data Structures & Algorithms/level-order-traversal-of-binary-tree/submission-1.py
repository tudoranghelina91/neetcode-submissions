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
        
        while q:
            level = []
            qlen = len(q)

            for i in range(qlen):
                crt = q.popleft()

                if not crt:
                    continue
                
                if crt.left:
                    q.append(crt.left)
                if crt.right:
                    q.append(crt.right)
                
                level.append(crt.val)
            
            if level:
                result.append(level)

        return result