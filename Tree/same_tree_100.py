"""
URL of problem:
https://leetcode.com/problems/same-tree/
"""


from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if bool(p) ^ bool(q):
            return False

        p_nodes, q_nodes = deque([p]), deque([q])
        while p_nodes and q_nodes:
            node_p, node_q = p_nodes.popleft(), q_nodes.popleft()
            if node_p.val != node_q.val:
                return False

            if bool(node_p.left) ^ bool(node_q.left):
                return False

            if node_p.left:
                p_nodes.append(node_p.left)
                q_nodes.append(node_q.left)

            if bool(node_p.right) ^ bool(node_q.right):
                return False

            if node_p.right:
                p_nodes.append(node_p.right)
                q_nodes.append(node_q.right)

        return True

    def isSameTree_2ndPass(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Time: O(n), Space: O(n)
        # Tags: Trees, BFS
        if not p and not q:
            return True

        queue_p, queue_q = deque([p]), deque([q])
        while queue_p and queue_q:
            p_node, q_node = queue_p.popleft(), queue_q.popleft()
            if bool(p_node) ^ bool(q_node):
                return False

            if not p_node:
                continue

            if p_node.val != q_node.val:
                return False

            queue_p.extend([p_node.left, p_node.right])
            queue_q.extend([q_node.left, q_node.right])

        if bool(queue_p) ^ bool(queue_q):
            return False

        return True
