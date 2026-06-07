# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list = []
    def get_leaf_values(self, root):
        if root==None:
            return 
        if root.right==None and root.left == None:
            self.list.append(root.val)
        self.get_leaf_values(root.right)
        self.get_leaf_values(root.left)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.get_leaf_values(root1)
        leaf_list1 = self.list
        self.list = []
        self.get_leaf_values(root2)
        leaf_list2 = self.list
        return leaf_list1==leaf_list2
            
        
        