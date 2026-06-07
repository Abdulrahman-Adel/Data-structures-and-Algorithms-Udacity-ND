# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.good = []
    def traverseTree(self, root, max):
        if root==None:
            return
        if root.val >= max:
            max = root.val
            self.good.append(root.val)
        self.traverseTree(root.right, max)
        self.traverseTree(root.left, max)

    def goodNodes(self, root: TreeNode) -> int:
        self.traverseTree(root, float('-inf'))
        return len(self.good)