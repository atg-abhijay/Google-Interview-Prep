"""
URL of problem:
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue, traversal = deque([root]), [[]]
        currently_added, upper_bound = 0, 1
        increment = 0
        while queue:
            node = queue.popleft()
            if currently_added < upper_bound:
                traversal[-1].append(node.val)
                currently_added += 1
            else:
                traversal.append([node.val])
                currently_added = 1
                upper_bound = increment
                increment = 0

            if node.left:
                queue.append(node.left)
                increment += 1

            if node.right:
                queue.append(node.right)
                increment += 1

        return traversal


    def levelOrder_2ndPass(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return [[]]


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(13)
    root.left.right = TreeNode(18)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root))


if __name__ == "__main__":
    main()
