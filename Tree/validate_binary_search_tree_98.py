"""
URL of problem:
https://leetcode.com/problems/validate-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        traversal = self.performInOrderTraversal(root)
        for current_idx in range(len(traversal)-1):
            if traversal[current_idx] >= traversal[current_idx+1]:
                return False

        return True


    def performInOrderTraversal(self, root):
        traversal = []
        if root.left:
            traversal.extend(self.performInOrderTraversal(root.left))
        traversal.append(root.val)
        if root.right:
            traversal.extend(self.performInOrderTraversal(root.right))

        return traversal


    def isValidBST_2ndPass(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.doInOrderTraversal(root, [float('-inf')])


    def doInOrderTraversal(self, root, traversal):
        if not root:
            return True

        if not self.doInOrderTraversal(root.left, traversal):
            return False

        if traversal[-1] >= root.val:
            return False

        traversal.append(root.val)
        if not self.doInOrderTraversal(root.right, traversal):
            return False

        return True


def main():
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    print(Solution().isValidBST_2ndPass(root))


if __name__ == "__main__":
    main()
