# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            if (root1 and not root2) or (not root1 and root2):
                return False
            if not root1 and not root2:
                return True
            
            return (root1.val == root2.val) and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

        if (root and not subRoot) or (not root and subRoot):
            return False
        if not root and not subRoot:
            return True
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)