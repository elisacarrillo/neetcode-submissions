# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = length of longest path between any two nodes within the tree
        # use bfs here -> looking for max depth
        self.diameter = 0
        def dfs(node):
            left = 0
            right = 0
            if (node.left):
                left=dfs(node.left)
            if (node.right):
                right =dfs(node.right)
            self.diameter = max(self.diameter, left + right)

            return 1 + max(left,right)
                    
            
        
        dfs(root)
        return self.diameter
        