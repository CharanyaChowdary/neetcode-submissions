# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q=deque([root])
        depth=0
        while q:
            levelsize=len(q)
            for i in range(levelsize):
                node=q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            depth+=1
        return depth
        