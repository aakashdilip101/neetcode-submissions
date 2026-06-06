# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def check_depth(root: Optional[TreeNode], current_depth: int):
            if not root:
                return current_depth
            
            current_depth += 1
            return max(current_depth, check_depth(root.left, current_depth), check_depth(root.right, current_depth))
        
        return check_depth(root, 0)
        