from collections import defaultdict
from pprint import pprint
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # I think the most difficult part with this problem is that the path doesn't have to start from the root
        # so you have to double run your algorithm treating each node as root to compute the paths
        # so run a dfs and while on current node run another one but with this one caclute the sum so far
        
        # this algorithm runs on O(nlogn) or O(n^2)
        # self.total = 0
        # def helper(node, sumSoFar):
        #     if not node:
        #         return 
        #     sumSoFar += node.val
        #     if sumSoFar == targetSum:
        #         self.total += 1
        #     helper(node.right, sumSoFar)
        #     helper(node.left, sumSoFar)
        
        # def dfs(node):
        #     if not node:
        #         return
        #     helper(node, 0)
        #     dfs(node.right)
        #     dfs(node.left)
        
        # dfs(root)
        # return self.total

        # 
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val
            count = prefix_sums.get(current_sum - targetSum, 0)

            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            prefix_sums[current_sum] -= 1

            return count

        prefix_sums = {0: 1}
        return dfs(root, 0)
            


        

