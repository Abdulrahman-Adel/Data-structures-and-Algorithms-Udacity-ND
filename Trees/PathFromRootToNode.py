# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:16:45 2020

@author: Abdelrahman
"""


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def path_from_root_to_node(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    from root to the data node
    """
    if root.data == data:  # Value found
        return [data]

    if (root.left is None) and (root.right) is None:  # Not found in this branch and no more depth
        return []

    left_findings = [root.data]
    right_findings = [root.data]

    if root.left is not None:
        left_findings.extend(path_from_root_to_node(root.left, data))

    if root.right is not None:
        right_findings.extend(path_from_root_to_node(root.right, data))

    if len(left_findings) > 1:
        return left_findings
    elif len(right_findings) > 1:
        return right_findings
    else:
        return []