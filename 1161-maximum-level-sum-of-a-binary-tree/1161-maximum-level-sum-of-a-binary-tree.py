# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        discovered = deque()

        maxSum = float('-inf')

        if root:
            discovered.append(root)

        i = 1
        maxLevel = 1
        while discovered:
            current = len(discovered)
            levelSum = 0
            for _ in range(current):
                if discovered[0].left:
                    discovered.append(discovered[0].left)
                if discovered[0].right:
                    discovered.append(discovered[0].right)
                levelSum += discovered.popleft().val
            
            if levelSum > maxSum:
                maxLevel = i
            maxSum = max(maxSum, levelSum)
            i+= 1
        print('Max Sum', maxSum) 
        
        return maxLevel
                