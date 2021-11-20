"""
URL of problem:
https://leetcode.com/problems/balanced-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left_hgt = self.determineHeight(root.left)
        right_hgt = self.determineHeight(root.right)

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        return abs(left_hgt - right_hgt) <= 1 and left_balanced and right_balanced


    def determineHeight(self, root):
        if not root:
            return 0

        return 1 + max(self.determineHeight(root.left), self.determineHeight(root.right))


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().isBalanced(root))


if __name__ == "__main__":
    main()
