# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def appendToLevel(curr: Optional[TreeNode], currLevel: int, maxLevel: int, nodes: List[List[int]]):
            if not curr:
                return nodes
            
            try:
                nodes[currLevel].append(curr.val)
            except:
                nodes.append([])
                nodes[currLevel].append(curr.val)

            currLevel += 1

            nodes = appendToLevel(curr.left, currLevel, maxLevel, nodes)
            nodes = appendToLevel(curr.right, currLevel, maxLevel, nodes)

            return nodes
    
        if not root:
            return []

        nodes = [[]]
        currLevel = 0
        nodes[0].append(root.val)
        nodes = appendToLevel(root.left, 1, 1, nodes)
        nodes = appendToLevel(root.right, 1, 1, nodes)
        return nodes
            