"""
URL of problem:
https://leetcode.com/problems/redundant-connection/
"""


from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(set)
        for node_u, node_v in edges:
            graph[node_u].add(node_v)
            graph[node_v].add(node_u)

        extra_edge = None
        for node_u, node_v in edges:
            if graph[node_u] - {node_v} and graph[node_v] - {node_u}:
                extra_edge = [node_u, node_v]

        return extra_edge


def main():
    print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))


if __name__ == "__main__":
    main()
