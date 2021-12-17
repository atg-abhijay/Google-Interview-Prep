"""
URL of problem:
https://leetcode.com/problems/redundant-connection/
"""


from collections import defaultdict, deque
from itertools import chain


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        components = defaultdict(set)
        node_cmpts = defaultdict(lambda: float('inf'))
        curr_val = 1
        for node_u, node_v in edges:
            u_cmpt, v_cmpt = node_cmpts[node_u], node_cmpts[node_v]
            # Nodes that belong to the same
            # components as nodes u and v respectively
            u_nodes, v_nodes = components[u_cmpt], components[v_cmpt]
            if u_cmpt == v_cmpt != float('inf'):
                return [node_u, node_v]

            cmpt_val = min(curr_val, u_cmpt, v_cmpt)
            components[cmpt_val].update([node_u, node_v])
            node_cmpts[node_u] = node_cmpts[node_v] = cmpt_val
            components[cmpt_val].update(*[u_nodes, v_nodes])

            cmpt_to_clear = float('inf')
            if cmpt_val == curr_val:
                curr_val += 1
                nodes_to_update = [u_nodes, v_nodes]
            elif cmpt_val == u_cmpt:
                nodes_to_update = [v_nodes]
                cmpt_to_clear = v_cmpt
            else:
                nodes_to_update = [u_nodes]
                cmpt_to_clear = u_cmpt

            for node in chain(*nodes_to_update):
                node_cmpts[node] = cmpt_val

            components[cmpt_to_clear].clear()


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
