"""
URL of problem:
https://leetcode.com/problems/subtree-of-another-tree/
"""


from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False


    def isSameTree(self, p_root, q_root):
        p_nodes, q_nodes = deque([p_root]), deque([q_root])
        while p_nodes and q_nodes:
            p_node, q_node = p_nodes.popleft(), q_nodes.popleft()

            if p_node.val != q_node.val:
                return False

            if bool(p_node.left) ^ bool(q_node.left):
                return False

            if p_node.left:
                p_nodes.append(p_node.left)
                q_nodes.append(q_node.left)

            if bool(p_node.right) ^ bool(q_node.right):
                return False

            if p_node.right:
                p_nodes.append(p_node.right)
                q_nodes.append(q_node.right)

        return True


    def isSubtree_2ndPass(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        tree_nodes = deque([root])
        same_trees = False
        while tree_nodes:
            node = tree_nodes.popleft()
            if node.val == subRoot.val:
                same_trees |= self.areSameTrees(node, subRoot)

            if node.left:
                tree_nodes.append(node.left)
            if node.right:
                tree_nodes.append(node.right)

        return same_trees


    def areSameTrees(self, root_p, root_q):
        p_nodes, q_nodes = deque([root_p]), deque([root_q])
        while p_nodes and q_nodes:
            p_node, q_node = p_nodes.popleft(), q_nodes.popleft()
            if bool(p_node) ^ bool(q_node):
                return False

            if not p_node:
                continue

            if p_node.val != q_node.val:
                return False

            p_nodes.extend([p_node.left, p_node.right])
            q_nodes.extend([q_node.left, q_node.right])

        if bool(p_nodes) ^ bool(q_nodes):
            return False

        return True


def main():
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
    print(Solution().isSubtree_2ndPass(root, sub_root))


if __name__ == "__main__":
    main()
