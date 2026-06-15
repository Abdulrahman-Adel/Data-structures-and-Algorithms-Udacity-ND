# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        # self.MaxRoute = 0
        
        
        # def maxZigZag(node, route, prev):
        #     if not node:
        #         return
        #     self.MaxRoute = max(self.MaxRoute, route)
        #     if prev=='r':
        #         maxZigZag(node.left, route + 1, 'l')
        #     elif prev=='l':
        #         maxZigZag(node.right,  route + 1, 'r')
        
        # def dfs(node):
        #     if not node:
        #         return
            
        #     maxZigZag(node, 0, 'r')
        #     maxZigZag(node, 0, 'l')
            
        #     dfs(node.right)
        #     dfs(node.left)

            
            
        # dfs(root)
        # return self.MaxRoute

        
        def dfs(root):
            if not root: return [-1, -1, -1]
            left, right = dfs(root.left), dfs(root.right)
            return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]
        return dfs(root)[-1]
            
