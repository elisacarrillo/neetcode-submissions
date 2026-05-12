# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        res = []
        queue.append(root)
        level = []
        if (root is None):
            return []
        while len(queue) > 0:
            level = len(queue)
            
            for i in range(level):
                node = queue.pop(0)
                if (i == level - 1):
                    res.append(node.val) 


                if (node.left):
                    queue.append(node.left) 
                if (node.right):
                    queue.append(node.right)
                
                          

            
            
            
        return res
            
            

        