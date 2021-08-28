"""
URL of problem:
https://leetcode.com/problems/clone-graph/
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        if not node.neighbors:
            return Node(node.val)

        cloned_nodes = [Node(i) for i in range(0, 101)]
        visited_nodes = [0] * 101
        queue = [node]
        visited_nodes[1] = 1
        while queue:
            node_to_clone = queue.pop()
            for nbr in node_to_clone.neighbors:
                cloned_nodes[node_to_clone.val].neighbors.append(cloned_nodes[nbr.val])
                if not visited_nodes[nbr.val]:
                    visited_nodes[nbr.val] = 1
                    queue.append(nbr)

        return cloned_nodes[1]


def main():
    a = Node(1, [])
    b = Node(2, [])
    a.neighbors.append(b)
    b.neighbors.append(a)
    print(Solution().cloneGraph(a))


if __name__ == "__main__":
    main()
