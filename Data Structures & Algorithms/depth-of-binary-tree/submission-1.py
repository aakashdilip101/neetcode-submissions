# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root: Optional[TreeNode], curr_depth: int):
            if not root:
                return curr_depth
            
            curr_depth += 1
            return max(curr_depth, depth(root.left, curr_depth), depth(root.right, curr_depth))
        
        return depth(root, 0)
        