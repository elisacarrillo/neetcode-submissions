# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        visited = set()
        def dfs(tNode: Optional[TreeNode], visited):
            if (tNode is None):
                return 0
            if (tNode not in visited):
                visited.add(tNode)
                lefty = dfs(tNode.left, visited) 
                righty = dfs(tNode.right, visited) 
                return max(lefty, righty) + 1
        left = 0
        right = 0
        return dfs(root, visited)


        