# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#brute force approach

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return 0
            return 1+max(height(root.right),height(root.left))
        if root is None:
            return 0
        lheight=height(root.left)
        rheight=height(root.right)
        rdiameter=self.diameterOfBinaryTree(root.right)
        ldiameter=self.diameterOfBinaryTree(root.left)
        return max(lheight+rheight,rdiameter,ldiameter)

            

        