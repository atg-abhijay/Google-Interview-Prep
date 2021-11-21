"""
URL of problem:
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""


from collections import deque
import heapq


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        TreeNode.__lt__ = lambda self, other: other.val < self.val
        heap, num_nodes = [], 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            heapq.heappush(heap, node)
            num_nodes += 1
            if num_nodes > k:
                heapq.heappop(heap)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return heap[0].val


    def kthSmallest_2ndPass(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        in_order_traversal = self.doInOrderTraversal(root, [])
        return in_order_traversal[k-1]


    def doInOrderTraversal(self, root, traversal):
        if not root:
            return

        self.doInOrderTraversal(root.left, traversal)
        traversal.append(root.val)
        self.doInOrderTraversal(root.right, traversal)

        return traversal


def main():
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    print(Solution().kthSmallest(root, 3))


if __name__ == "__main__":
    main()
