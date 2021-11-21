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
        # Time: O(n), Space: O(1)
        # Tags: Trees

        # Approach learnt using this LeetCode discussion post:
        # https://leetcode.com/problems/balanced-binary-tree/discuss/35691/The-bottom-up-O(N)-solution-would-be-better
        if not root:
            return True

        return self.runDFS(root) != -1


    def runDFS(self, root):
        if not root:
            return 0

        left_hgt = self.runDFS(root.left)
        right_hgt = self.runDFS(root.right)

        if abs(left_hgt - right_hgt) > 1:
            return -1

        if left_hgt == -1 or right_hgt == -1:
            return -1

        return 1 + max(left_hgt, right_hgt)


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().isBalanced(root))


if __name__ == "__main__":
    main()
