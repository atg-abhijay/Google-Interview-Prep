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
        return self.doInOrderTraversal(root, float('-inf'))[1]


    def doInOrderTraversal(self, root, curr_value):
        # Time: O(n), Space: O(1)
        # Tags: Trees
        if not root:
            return curr_value, True

        curr_value, sub_result = self.doInOrderTraversal(root.left, curr_value)
        if not sub_result:
            return curr_value, False

        if curr_value >= root.val:
            return curr_value, False

        curr_value = root.val
        curr_value, sub_result = self.doInOrderTraversal(root.right, curr_value)
        if not sub_result:
            return curr_value, False

        return curr_value, sub_result


def main():
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    print(Solution().isValidBST_2ndPass(root))


if __name__ == "__main__":
    main()
