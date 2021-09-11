"""
URL of problem:
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.determineMaxSum(root, dict())


    def determineMaxSum(self, root, nodes_sum):
        max_sum = float('-inf')
        if not root.left and not root.right:
            nodes_sum[root] = root.val
            return root.val

        left_value, right_value = 0, 0
        if root.left:
            max_sum = max(max_sum, self.determineMaxSum(root.left, nodes_sum))
            left_value = nodes_sum[root.left]
        if root.right:
            max_sum = max(max_sum, self.determineMaxSum(root.right, nodes_sum))
            right_value = nodes_sum[root.right]

        nodes_sum[root] = max([
            root.val, root.val + left_value, root.val + right_value
        ])

        max_sum = max([
            max_sum, nodes_sum[root], root.val + left_value + right_value
        ])

        return max_sum
