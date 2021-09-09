"""
URL of problem:
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_depth = 1
        max_depth += max(self.maxDepth(root.left), self.maxDepth(root.right))

        return max_depth
