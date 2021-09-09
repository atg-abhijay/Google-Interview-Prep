"""
URL of problem:
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


from collections import deque


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


    def maxDepthIterativeBFS(self, root: TreeNode) -> int:
        # Since the values of the nodes are not
        # being used, store the depths in them
        if not root:
            return 0

        nodes_deque = deque([root])
        max_depth = 1
        root.val = max_depth
        while nodes_deque:
            node = nodes_deque.popleft()
            if node.left:
                node.left.val = node.val + 1
                nodes_deque.append(node.left)

            if node.right:
                node.right.val = node.val + 1
                nodes_deque.append(node.right)

            max_depth = max(max_depth, node.val)

        return max_depth
