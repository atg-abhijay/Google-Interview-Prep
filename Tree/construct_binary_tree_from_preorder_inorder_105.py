"""
URL of problem:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return None


def main():
    print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).val)


if __name__ == "__main__":
    main()
