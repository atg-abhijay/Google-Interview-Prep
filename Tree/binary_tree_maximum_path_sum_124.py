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
        """
        Keep track of the max sum possible at each node
        in a dictionary. For this sum, assume that the
        node is part of the sum and then find the best
        value for that node amongst [node, node + right,
        node + left] but not node + right + left.

        If node + right + left is selected at any point,
        then the parent of node cannot build a path with
        node since node + right + left is already a path
        in and of itself.

        Doing it this way allows parent nodes to continue
        building paths using their children because the
        max sum of the child was found by actually using
        the child in each possible case. This helps avoid
        having to check for disconnected parents and max sums.

        Use a separate variable max_sum to keep track of the
        actual max path sum that takes into account the max
        sum for the node and also node + right + left.
        """
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


    def maxPathSum_2ndPass(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.determineMaxSumAtNode(root)[1]


    def determineMaxSumAtNode(self, node):
        if not node:
            return 0, float('-inf')

        left_sum, max_left = self.determineMaxSumAtNode(node.left)
        right_sum, max_right = self.determineMaxSumAtNode(node.right)

        node_sum = max(node.val + left_sum, node.val + right_sum, node.val)
        max_overall = max(max_left, max_right, node_sum, node.val + left_sum + right_sum)
        return node_sum, max_overall


def main():
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().maxPathSum_2ndPass(root))


if __name__ == "__main__":
    main()
