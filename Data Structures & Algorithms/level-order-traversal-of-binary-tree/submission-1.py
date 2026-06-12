# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []

        def appendToLevel(curr: Optional[TreeNode], currLevel: int):
            if not curr:
                return
            
            if len(nodes) == currLevel:
                nodes.append([])
            
            nodes[currLevel].append(curr.val)

            appendToLevel(curr.left, currLevel + 1)
            appendToLevel(curr.right, currLevel + 1)

        appendToLevel(root, 0)
        return nodes
            