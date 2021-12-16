"""
URL of problem:
https://leetcode.com/problems/redundant-connection/
"""


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        extra_edge = []
        visited_nodes = set()
        for node_u, node_v in edges:
            if node_u in visited_nodes and node_v in visited_nodes:
                extra_edge = [node_u, node_v]
            else:
                visited_nodes.add(node_u)
                visited_nodes.add(node_v)

        return extra_edge


def main():
    print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))


if __name__ == "__main__":
    main()
