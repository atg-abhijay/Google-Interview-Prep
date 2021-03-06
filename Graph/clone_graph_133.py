"""
URL of problem:
https://leetcode.com/problems/clone-graph/
"""


from collections import deque


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
        # Let n be #nodes and m be #edges
        # Time: O(n + 2m), Space: O(n + 2m)
        # (larger space actually since the
        # array has all possible nodes)
        # (the 'queue' here is actually a
        # stack => DFS)
        # Tags: Graphs, DFS
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


    def cloneGraph_2ndPass(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # Let n be #nodes and m be #edges
        # Time: O(n + 2m), Space: O(n + 2m)
        # Tags: Graphs, BFS

        # Empty graph
        if not node:
            return None

        # One node and no edges
        if not node.neighbors:
            return Node(1)

        first_clone = Node(1)
        clones = {1: first_clone}
        queue = deque([node])
        visited = set([1])
        while queue:
            curr_node = queue.popleft()
            for nbr in curr_node.neighbors:
                if not nbr.val in visited:
                    visited.add(nbr.val)
                    queue.append(nbr)

                if not nbr.val in clones:
                    clones[nbr.val] = Node(nbr.val)

                clones[curr_node.val].neighbors.append(clones[nbr.val])

        return first_clone


def main():
    a = Node(1, [])
    b = Node(2, [])
    a.neighbors.append(b)
    b.neighbors.append(a)
    print(Solution().cloneGraph(a))


if __name__ == "__main__":
    main()
