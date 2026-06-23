# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        discovered = deque()
        result = []
        test = deque()
        if root:
            discovered.append(root)
            test.append(root.val)
        while discovered:
            current = len(discovered)
            print('discovered: ', test)
            for j in range(current):
                if discovered and discovered[0].left:
                    discovered.append(discovered[0].left)
                    test.append(discovered[0].left.val)
                if discovered and discovered[0].right:
                    discovered.append(discovered[0].right)
                    test.append(discovered[0].right.val)
                if discovered and j == current - 1:
                    result.append(discovered[0].val)
                if discovered:
                    discovered.popleft()
                    test.popleft()
        return result

            
