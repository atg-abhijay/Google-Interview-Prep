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
        return False


def main():
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
    print(Solution().isSubtree_2ndPass(root, sub_root))


if __name__ == "__main__":
    main()
