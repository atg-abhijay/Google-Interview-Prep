"""
URL of problem:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root or q == root:
            return root

        path_p = self.findPath(root, p)
        path_q = self.findPath(root, q)

        least_common_ancestor = root
        for path_p_node, path_q_node in zip(path_p, path_q):
            if path_p_node == path_q_node:
                least_common_ancestor = path_p_node
            else:
                break

        return least_common_ancestor


    def findPath(self, root, target):
        path = [root]
        while 1:
            node = path[-1]
            if target.val < node.val:
                path.append(node.left)
            elif target.val > node.val:
                path.append(node.right)
            else:
                break

        return path
