# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(root):
            if root is None:
                return 0
            return 1+max(dfs(root.right),dfs(root.left))
        l_h=dfs(root.left)
        r_h=dfs(root.right)
        if abs(l_h-r_h)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        