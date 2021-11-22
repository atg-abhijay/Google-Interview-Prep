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
        if preorder == inorder:
            root = None
            for num in reversed(inorder):
                root = TreeNode(num, right=root)

            return root

        if not inorder:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(preorder[0])
        root_idx = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:], inorder[:root_idx])
        root.right = self.buildTree(preorder[2:], inorder[root_idx + 1:])

        return root


def main():
    print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).val)


if __name__ == "__main__":
    main()
