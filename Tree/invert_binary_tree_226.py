"""
URL of problem:
https://leetcode.com/problems/invert-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


    def invertTree_2ndPass(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Time: O(n), Space: O(1)
        # Tags: Trees, Recursion
        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
