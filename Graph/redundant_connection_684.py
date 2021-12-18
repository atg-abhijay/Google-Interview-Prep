"""
URL of problem:
https://leetcode.com/problems/redundant-connection/
"""


from collections import defaultdict
from itertools import chain


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        components = defaultdict(set)
        node_compts = defaultdict(lambda: float('inf'))
        curr_compt = 1
        for node_u, node_v in edges:
            u_compt, v_compt = node_compts[node_u], node_compts[node_v]
            # Nodes that belong to the same
            # components as nodes u and v respectively
            u_nodes, v_nodes = components[u_compt], components[v_compt]
            if u_compt == v_compt != float('inf'):
                return [node_u, node_v]

            min_compt = min(curr_compt, u_compt, v_compt)
            components[min_compt].update([node_u, node_v])
            node_compts[node_u] = node_compts[node_v] = min_compt
            components[min_compt].update(*[u_nodes, v_nodes])

            params = {
                curr_compt: [[u_nodes, v_nodes], float('inf')],
                u_compt: [[v_nodes], v_compt],
                v_compt: [[u_nodes], u_compt]
            }

            if min_compt == curr_compt:
                curr_compt += 1

            nodes_to_update, compt_to_clear = params[min_compt]
            for node in chain(*nodes_to_update):
                node_compts[node] = min_compt

            components[compt_to_clear].clear()


def main():
    print(
        Solution().findRedundantConnection(
            [
                [9, 10],
                [5, 8],
                [2, 6],
                [1, 5],
                [3, 8],
                [4, 9],
                [8, 10],
                [4, 10],
                [6, 8],
                [7, 9],
            ]
        )
    )


if __name__ == "__main__":
    main()
